"""Optional Test Observer integration.

When the ``TO_URL`` environment variable is set, this module registers a pytest
plugin that reports the test run and individual results to the Test Observer
REST API.

One test execution is created per category (Security, Reliability, …) the
first time a test from that category is encountered.  The execution's test
plan is named ``<TO_TEST_PLAN>-<category>`` (e.g. ``sunbeam-acceptance-security``).

Required environment variables (when ``TO_URL`` is set):
    TO_URL              Base URL of the Test Observer API.
    TO_SNAP_REVISION    Snap revision number (integer).

Optional environment variables:
    TO_SNAP_NAME        Snap name (default: ``openstack``).
    TO_SNAP_TRACK       Snap track (default: ``2024.1``).
    TO_SNAP_STAGE       Snap risk level: edge/beta/candidate/stable (default: ``edge``).
    TO_SNAP_VERSION     Version string (default: ``<track>/<stage>``).
    TO_SNAP_STORE       Snap store (default: ``ubuntu``).
    TO_ENVIRONMENT      Environment name (default: ``manual``).
    TO_TEST_PLAN        Test plan prefix (default: ``sunbeam-acceptance``).
    TO_ARCH             Architecture override (auto-detected if not set).
    TO_CI_LINK          URL of the CI job driving this run.
"""

from __future__ import annotations

import json
import logging
import os
import platform
from typing import Callable

logger = logging.getLogger("defining_acceptance.observer")

_PLAN_TAGS = frozenset(
    {"security", "reliability", "operations", "performance", "provisioning"}
)

_ARCH_MAP: dict[str, str] = {
    "x86_64": "amd64",
    "aarch64": "arm64",
    "armv7l": "armhf",
    "ppc64le": "ppc64el",
    "s390x": "s390x",
}


def _detect_arch() -> str:
    return _ARCH_MAP.get(platform.machine(), platform.machine())


class TestObserverPlugin:
    """Pytest plugin that streams test results to the Test Observer API.

    One test execution is created per test category (plan tag) the first time
    a result for that category arrives.  All executions are closed together at
    session end.
    """

    def __init__(
        self,
        client: object,
        make_body: Callable[[str], object],
        test_plan_prefix: str,
    ) -> None:
        self._client = client
        # Callable(test_plan_name) -> StartSnapTestExecutionRequest
        self._make_body = make_body
        self._test_plan_prefix = test_plan_prefix
        # category (capitalised) -> execution id
        self._executions: dict[str, int] = {}
        # categories that had at least one failure (for final status)
        self._category_failed: set[str] = set()
        # pytest nodeids already reported (to avoid duplicate from setup+call)
        self._settled: set[str] = set()
        # per-test SSH output accumulator
        self._io_lines: list[str] = []
        # category for the currently running item (set from pytest markers)
        self._current_category: str = ""

        # Intercept report.attach_text / attach_file so every command output
        # that SSHRunner emits is also captured into _io_lines for io_log.
        from defining_acceptance.reporting import report as _report

        plugin = self

        _orig_text = _report.attach_text
        _orig_file = _report.attach_file

        def _capture_text(content: str, name: str) -> None:
            _orig_text(content, name)
            text = "" if content is None else str(content)
            if text.strip():
                plugin._io_lines.append(f"### {name}\n{text}")

        def _capture_file(path: object, name: str) -> None:
            _orig_file(path, name)
            try:
                from pathlib import Path

                text = Path(str(path)).read_text(encoding="utf-8", errors="replace")
                if text.strip():
                    plugin._io_lines.append(f"### {name}\n{text}")
            except Exception:
                pass

        _report.attach_text = _capture_text  # type: ignore[method-assign]
        _report.attach_file = _capture_file  # type: ignore[method-assign]

    # ── Pytest hooks ──────────────────────────────────────────────────────────

    def pytest_runtest_setup(self, item: object) -> None:
        """Reset per-test state and extract the category from pytest markers."""
        self._io_lines = []
        self._current_category = ""
        get_marker = getattr(item, "get_closest_marker", None)
        if get_marker is not None:
            for tag in _PLAN_TAGS:
                if get_marker(tag) is not None:
                    self._current_category = tag.capitalize()
                    break

    def pytest_runtest_logreport(self, report: object) -> None:
        from defining_acceptance.clients.test_observer_client.models.test_result_request import (
            TestResultRequest,
        )
        from defining_acceptance.clients.test_observer_client.models.test_result_status import (
            TestResultStatus,
        )

        when = getattr(report, "when", None)
        # Use the raw pytest nodeid for dedup tracking (guaranteed unique).
        pytest_nodeid = getattr(report, "nodeid", "")

        # Category is derived from pytest markers in pytest_runtest_setup,
        # which is guaranteed to match the same marker set used by skip rules.
        category = self._current_category
        if not category:
            return  # skip non-BDD or uncategorised tests

        # Human-readable name: scenario title when available, nodeid otherwise.
        name = pytest_nodeid
        if scenario := getattr(report, "scenario", None):
            name = scenario["name"]

        execution_id = self._get_or_create_execution(category)
        if execution_id is None:
            return

        longrepr = getattr(report, "longrepr", None)
        io_log = str(longrepr) if longrepr else ""
        if self._io_lines:
            io_log += "\n\n" if io_log else ""
            io_log += "\n\n".join(self._io_lines)

        if when == "setup":
            if getattr(report, "failed", False):
                self._settled.add(pytest_nodeid)
                self._category_failed.add(category)
                self._post(
                    execution_id,
                    [
                        TestResultRequest(
                            name=name,
                            status=TestResultStatus.FAILED,
                            category=category,
                            io_log=io_log,
                        )
                    ],
                )
            elif getattr(report, "skipped", False):
                self._settled.add(pytest_nodeid)
                self._post(
                    execution_id,
                    [
                        TestResultRequest(
                            name=name,
                            status=TestResultStatus.SKIPPED,
                            category=category,
                            io_log=io_log,
                        )
                    ],
                )
            # setup passed → wait for the call phase

        elif when == "call":
            if pytest_nodeid in self._settled:
                return  # already reported from setup
            if getattr(report, "passed", False):
                status = TestResultStatus.PASSED
            elif getattr(report, "failed", False):
                status = TestResultStatus.FAILED
                self._category_failed.add(category)
            else:
                status = TestResultStatus.SKIPPED
            self._post(
                execution_id,
                [
                    TestResultRequest(
                        name=name,
                        status=status,
                        category=category,
                        io_log=io_log,
                    )
                ],
            )

    def pytest_sessionfinish(self, session: object, exitstatus: int) -> None:
        from defining_acceptance.clients.test_observer_client.api.test_executions import (
            patch_test_execution_v1_test_executions_id_patch as patch_api,
        )
        from defining_acceptance.clients.test_observer_client.models.test_execution_status import (
            TestExecutionStatus,
        )
        from defining_acceptance.clients.test_observer_client.models.test_executions_patch_request import (
            TestExecutionsPatchRequest,
        )

        interrupted = exitstatus == 2  # keyboard interrupt

        for category, execution_id in self._executions.items():
            if interrupted:
                status = TestExecutionStatus.ENDED_PREMATURELY
            elif category in self._category_failed:
                status = TestExecutionStatus.FAILED
            else:
                status = TestExecutionStatus.PASSED

            try:
                patch_api.sync(
                    execution_id,
                    client=self._client,
                    body=TestExecutionsPatchRequest(status=status),
                )
                logger.info(
                    "Test Observer: closed execution id=%d (category=%r) status=%s",
                    execution_id,
                    category,
                    status.value,
                )
            except Exception:
                logger.warning(
                    "Failed to close Test Observer execution %d (category=%r)",
                    execution_id,
                    category,
                    exc_info=True,
                )

    # ── Internal ──────────────────────────────────────────────────────────────

    def _get_or_create_execution(self, category: str) -> int | None:
        """Return the execution id for *category*, creating one if needed."""
        if category in self._executions:
            return self._executions[category]

        from defining_acceptance.clients.test_observer_client.api.test_executions import (
            start_test_execution_v1_test_executions_start_test_put as start_api,
        )

        test_plan = f"{self._test_plan_prefix}-{category.lower()}"
        try:
            response = start_api.sync_detailed(
                client=self._client,
                body=self._make_body(test_plan),
            )
            logger.debug("Received response: %s", response)  # Debug statement
        except Exception:
            logger.warning(
                "Failed to start Test Observer execution for category %r",
                category,
                exc_info=True,
            )
            return None

        if not (200 <= response.status_code.value < 300):
            logger.warning(
                "start-test for category %r returned HTTP %d (body: %r)",
                category,
                response.status_code.value,
                response.content[:200],
            )
            return None

        try:
            data = json.loads(response.content)
            execution_id = data["id"]
        except Exception:
            logger.warning(
                "Could not parse execution id for category %r from: %r",
                category,
                response.content,
            )
            return None

        self._executions[category] = execution_id
        logger.info(
            "Test Observer: started execution id=%d plan=%r",
            execution_id,
            test_plan,
        )
        return execution_id

    def _post(self, execution_id: int, results: list) -> None:
        from defining_acceptance.clients.test_observer_client.api.test_executions import (
            post_results_v1_test_executions_id_test_results_post as post_api,
        )

        try:
            post_api.sync(execution_id, client=self._client, body=results)
        except Exception:
            names = ", ".join(r.name for r in results)
            logger.warning("Failed to post result(s) for %s", names, exc_info=True)


def create_plugin() -> TestObserverPlugin | None:
    """Build a :class:`TestObserverPlugin` from environment variables.

    Returns ``None`` (silently) when ``TO_URL`` is not set, or logs a warning
    and returns ``None`` when required variables are missing.

    No network call is made here; executions are created lazily on first use
    per category.
    """
    to_url = os.environ.get("TO_URL")
    if not to_url:
        return None

    try:
        from defining_acceptance.clients.test_observer_client import Client
        from defining_acceptance.clients.test_observer_client.models.snap_stage import (
            SnapStage,
        )
        from defining_acceptance.clients.test_observer_client.models.start_snap_test_execution_request import (
            StartSnapTestExecutionRequest,
        )
        from defining_acceptance.clients.test_observer_client.models.test_execution_relevant_link_create import (
            TestExecutionRelevantLinkCreate,
        )
        from defining_acceptance.clients.test_observer_client.models.test_execution_status import (
            TestExecutionStatus,
        )
        from defining_acceptance.clients.test_observer_client.types import UNSET
    except ImportError:
        logger.warning(
            "Test Observer dependencies not installed (httpx, attrs). "
            "Install the 'to' dependency group to enable TO reporting."
        )
        return None

    revision_str = os.environ.get("TO_SNAP_REVISION", "")
    if not revision_str:
        logger.warning("TO_SNAP_REVISION not set; Test Observer registration skipped")
        return None
    try:
        revision = int(revision_str)
    except ValueError:
        logger.warning(
            "TO_SNAP_REVISION=%r is not a valid integer; Test Observer registration skipped",
            revision_str,
        )
        return None

    snap_stage_str = os.environ.get("TO_SNAP_STAGE", "edge")
    try:
        snap_stage = SnapStage(snap_stage_str)
    except ValueError:
        logger.warning(
            "TO_SNAP_STAGE=%r is not valid (edge/beta/candidate/stable); "
            "Test Observer registration skipped",
            snap_stage_str,
        )
        return None

    snap_track = os.environ.get("TO_SNAP_TRACK", "2024.1")
    snap_name = os.environ.get("TO_SNAP_NAME", "openstack")
    snap_version = os.environ.get("TO_SNAP_VERSION") or f"{snap_track}/{snap_stage_str}"
    snap_store = os.environ.get("TO_SNAP_STORE", "ubuntu")
    environment = os.environ.get("TO_ENVIRONMENT", "manual")
    test_plan_prefix = os.environ.get("TO_TEST_PLAN", "sunbeam-acceptance")
    arch = os.environ.get("TO_ARCH") or _detect_arch()
    ci_link = os.environ.get("TO_CI_LINK") or None
    ci_link = "http://myci.com/job/125"
    relevant_links = (
        [TestExecutionRelevantLinkCreate(label="CI job", url=ci_link)]
        if ci_link
        else UNSET
    )

    def make_body(test_plan: str) -> StartSnapTestExecutionRequest:
        return StartSnapTestExecutionRequest(
            name=snap_name,
            version=snap_version,
            arch=arch,
            environment=environment,
            test_plan=test_plan,
            initial_status=TestExecutionStatus.IN_PROGRESS,
            relevant_links=relevant_links,
            family="snap",
            revision=revision,
            track=snap_track,
            store=snap_store,
            execution_stage=snap_stage,
            ci_link=ci_link + "#" + test_plan or UNSET,
        )

    client = Client(base_url=to_url)
    logger.info(
        "Test Observer: configured, executions will be created per category at %s",
        to_url,
    )
    return TestObserverPlugin(
        client=client,
        make_body=make_body,
        test_plan_prefix=test_plan_prefix,
    )
