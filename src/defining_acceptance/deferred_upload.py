"""CLI tool to upload deferred Test Observer results."""

import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, cast

logger = logging.getLogger(__name__)


def upload(deferred_dir: Path, to_url: str) -> int:
    """Upload all category subdirectories in deferred_dir to Test Observer.

    Returns the number of categories successfully started (not necessarily
    fully uploaded — errors in result posting are logged but don't count
    against the return value).
    """
    from defining_acceptance.clients.test_observer_client import Client as _Client
    from defining_acceptance.clients.test_observer_client.api.test_executions import (
        patch_test_execution_v1_test_executions_id_patch as patch_api,
    )
    from defining_acceptance.clients.test_observer_client.api.test_executions import (
        post_results_v1_test_executions_id_test_results_post as post_api,
    )
    from defining_acceptance.clients.test_observer_client.api.test_executions import (
        post_status_update_v1_test_executions_id_status_update_post as status_api,
    )
    from defining_acceptance.clients.test_observer_client.api.test_executions import (
        start_test_execution_v1_test_executions_start_test_put as start_api,
    )
    from defining_acceptance.clients.test_observer_client.models.start_snap_test_execution_request import (
        StartSnapTestExecutionRequest as _StartSnapTestExecutionRequest,
    )
    from defining_acceptance.clients.test_observer_client.models.status_update_request import (
        StatusUpdateRequest as _StatusUpdateRequest,
    )
    from defining_acceptance.clients.test_observer_client.models.test_event_response import (
        TestEventResponse as _TestEventResponse,
    )
    from defining_acceptance.clients.test_observer_client.models.test_execution_status import (
        TestExecutionStatus as _TestExecutionStatus,
    )
    from defining_acceptance.clients.test_observer_client.models.test_executions_patch_request import (
        TestExecutionsPatchRequest as _TestExecutionsPatchRequest,
    )
    from defining_acceptance.clients.test_observer_client.models.test_result_request import (
        TestResultRequest as _TestResultRequest,
    )

    Client = cast(Any, _Client)
    StartSnapTestExecutionRequest = cast(Any, _StartSnapTestExecutionRequest)
    TestExecutionStatus = cast(Any, _TestExecutionStatus)
    TestExecutionsPatchRequest = cast(Any, _TestExecutionsPatchRequest)
    TestResultRequest = cast(Any, _TestResultRequest)
    start_sync_detailed = cast(Any, start_api.sync_detailed)
    post_sync = cast(Any, post_api.sync)
    patch_sync = cast(Any, patch_api.sync)
    status_sync = cast(Any, status_api.sync)
    StatusUpdateRequest = cast(Any, _StatusUpdateRequest)
    TestEventResponse = cast(Any, _TestEventResponse)

    client = Client(base_url=to_url)
    cat_dirs = sorted(p for p in deferred_dir.iterdir() if p.is_dir())

    # Phase 1 — Start all executions
    executions: dict[Path, int] = {}
    for cat_dir in cat_dirs:
        start_file = cat_dir / "start.json"
        if not start_file.exists():
            logger.warning("Skipping %s: missing start.json", cat_dir.name)
            continue

        try:
            start_data = json.loads(start_file.read_text())
            response = start_sync_detailed(
                client=client,
                body=StartSnapTestExecutionRequest.from_dict(start_data),
            )
            if not (200 <= response.status_code.value < 300):
                logger.error(
                    "start-test for %s returned HTTP %d: %r",
                    cat_dir.name,
                    response.status_code.value,
                    response.content[:200],
                )
                continue
            execution_id = json.loads(response.content)["id"]
            logger.info("Created execution id=%d for %s", execution_id, cat_dir.name)
        except Exception:
            logger.error(
                "Failed to start execution for %s", cat_dir.name, exc_info=True
            )
            continue

        executions[cat_dir] = execution_id

    # Phase 2 — Post results and status updates for all started executions
    for cat_dir, execution_id in executions.items():
        results_file = cat_dir / "results.jsonl"
        if results_file.exists():
            try:
                results = [
                    TestResultRequest.from_dict(json.loads(line))
                    for line in results_file.read_text().splitlines()
                    if line.strip()
                ]
                if results:
                    post_sync(execution_id, client=client, body=results)
                    logger.info(
                        "Posted %d result(s) for %s", len(results), cat_dir.name
                    )
            except Exception:
                logger.error(
                    "Failed to post results for %s", cat_dir.name, exc_info=True
                )

        status_file = cat_dir / "status_updates.jsonl"
        if status_file.exists():
            try:
                events = [
                    TestEventResponse.from_dict(json.loads(line))
                    for line in status_file.read_text().splitlines()
                    if line.strip()
                ]
                if events:
                    status_sync(
                        execution_id,
                        client=client,
                        body=StatusUpdateRequest(events=events),
                    )
                    logger.info(
                        "Posted %d status update(s) for %s",
                        len(events),
                        cat_dir.name,
                    )
            except Exception:
                logger.error(
                    "Failed to post status updates for %s", cat_dir.name, exc_info=True
                )

    # Phase 3 — Close all started executions
    for cat_dir, execution_id in executions.items():
        patch_file = cat_dir / "patch.json"
        if patch_file.exists():
            try:
                patch_body = TestExecutionsPatchRequest.from_dict(
                    json.loads(patch_file.read_text())
                )
            except Exception:
                logger.warning(
                    "Could not parse patch.json for %s; using ENDED_PREMATURELY",
                    cat_dir.name,
                )
                patch_body = TestExecutionsPatchRequest(
                    status=TestExecutionStatus.ENDED_PREMATURELY
                )
        else:
            logger.warning(
                "No patch.json for %s; using ENDED_PREMATURELY", cat_dir.name
            )
            patch_body = TestExecutionsPatchRequest(
                status=TestExecutionStatus.ENDED_PREMATURELY
            )

        try:
            patch_sync(execution_id, client=client, body=patch_body)
            logger.info("Closed execution %d for %s", execution_id, cat_dir.name)
        except Exception:
            logger.error(
                "Failed to close execution %d for %s",
                execution_id,
                cat_dir.name,
                exc_info=True,
            )

    return len(executions)


def main() -> None:
    import argparse

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    parser = argparse.ArgumentParser(
        description="Upload deferred Test Observer results to the API.",
        epilog="Example:\n  to-upload /tmp/to-deferred --to-url https://test-observer-api.canonical.com",
    )
    parser.add_argument("directory", help="Path to the deferred upload directory")
    parser.add_argument(
        "--to-url",
        default=os.environ.get("TO_URL"),
        help="Test Observer base URL (default: $TO_URL)",
    )
    args = parser.parse_args()

    if not args.to_url:
        print("Error: --to-url or TO_URL env var required", file=sys.stderr)
        sys.exit(1)

    if args.to_url.startswith("file://"):
        print("Error: --to-url must be an HTTP(S) URL for upload", file=sys.stderr)
        sys.exit(1)

    deferred_dir = Path(args.directory)
    if not deferred_dir.is_dir():
        print(f"Error: {deferred_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    n = upload(deferred_dir, args.to_url)
    print(f"Uploaded {n} category/categories.")
    if n == 0:
        sys.exit(1)
