from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deb_stage import DebStage
from ..models.test_execution_status import TestExecutionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_execution_relevant_link_create import (
        TestExecutionRelevantLinkCreate,
    )


T = TypeVar("T", bound="StartDebTestExecutionRequest")


@_attrs_define
class StartDebTestExecutionRequest:
    """
    Attributes:
        name (str): User-defined name identifying the artefact under test. Not unique - multiple versions/stages of the
            same artefact share this name. Examples: 'core22', 'ubuntu-desktop', 'snapd'
        version (str): Version identifier of the artefact being tested. Format depends on artefact family - e.g.,
            revisions for charms/snaps, version numbers for debs.
        arch (str): CPU architecture where tests will execute. Common values: 'amd64', 'arm64', 'armhf', 's390x',
            'ppc64el'
        environment (str): Name of the test execution environment. This can identify the specific physical device, VM,
            or container where tests run or logical environment like a test lab or cloud region. Examples: 'cm3', 'rpi4',
            'lxd-vm', 'aws-ec2'. The environment will be auto-created if it doesn't exist.
        test_plan (str): Identifier for the test suite or plan executed. Groups related test results together - e.g.,
            'certification-24.04', 'smoke-tests', 'full-regression'. The test plan will be auto-created if it doesn't exist.
        family (Literal['deb']):
        series (str): Ubuntu release series being tested. Examples: 'focal' (20.04), 'jammy' (22.04), 'noble' (24.04),
            'oracular' (24.10)
        repo (str): Repository containing the deb package. Examples: 'main', 'universe', 'restricted', 'multiverse' for
            archive repositories, or custom PPA names like 'ppa:team/ppa-name'
        ci_link (None | str | Unset): Optional URL linking to the CI job executing these tests. Useful for tracking test
            runs back to their automation source. Can be omitted.
        initial_status (TestExecutionStatus | Unset):
        relevant_links (list[TestExecutionRelevantLinkCreate] | Unset): Optional list of additional URLs related to this
            test execution (e.g., bug reports, documentation, related PRs). Can be omitted or left empty.
        needs_assignment (bool | Unset): Whether the artefact created from this test execution requires assignment of a
            reviewer. Set to true if test results need human review before the artefact can be promoted. Default false means
            no review assignment needed. Default: False.
        source (str | Unset): Source package name for PPA builds, or empty string for archive pockets. Provide this OR
            execution_stage, not both. Use source when testing from a PPA, use execution_stage when testing from official
            archive pockets. Default: ''.
        execution_stage (DebStage | Literal[''] | Unset): Archive pocket where the deb resides, or empty string for
            PPAs. Options: 'proposed' (pre-release testing area), 'updates' (stable updates). Provide this OR source, not
            both. Use execution_stage for official archive testing, leave empty if testing from a PPA (and provide source
            instead). Default: ''.
    """

    name: str
    version: str
    arch: str
    environment: str
    test_plan: str
    family: Literal["deb"]
    series: str
    repo: str
    ci_link: None | str | Unset = UNSET
    initial_status: TestExecutionStatus | Unset = UNSET
    relevant_links: list[TestExecutionRelevantLinkCreate] | Unset = UNSET
    needs_assignment: bool | Unset = False
    source: str | Unset = ""
    execution_stage: DebStage | Literal[""] | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        version = self.version

        arch = self.arch

        environment = self.environment

        test_plan = self.test_plan

        family = self.family

        series = self.series

        repo = self.repo

        ci_link: None | str | Unset
        if isinstance(self.ci_link, Unset):
            ci_link = UNSET
        else:
            ci_link = self.ci_link

        initial_status: str | Unset = UNSET
        if not isinstance(self.initial_status, Unset):
            initial_status = self.initial_status.value

        relevant_links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.relevant_links, Unset):
            relevant_links = []
            for relevant_links_item_data in self.relevant_links:
                relevant_links_item = relevant_links_item_data.to_dict()
                relevant_links.append(relevant_links_item)

        needs_assignment = self.needs_assignment

        source = self.source

        execution_stage: Literal[""] | str | Unset
        if isinstance(self.execution_stage, Unset):
            execution_stage = UNSET
        elif isinstance(self.execution_stage, DebStage):
            execution_stage = self.execution_stage.value
        else:
            execution_stage = self.execution_stage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "version": version,
                "arch": arch,
                "environment": environment,
                "test_plan": test_plan,
                "family": family,
                "series": series,
                "repo": repo,
            }
        )
        if ci_link is not UNSET:
            field_dict["ci_link"] = ci_link
        if initial_status is not UNSET:
            field_dict["initial_status"] = initial_status
        if relevant_links is not UNSET:
            field_dict["relevant_links"] = relevant_links
        if needs_assignment is not UNSET:
            field_dict["needs_assignment"] = needs_assignment
        if source is not UNSET:
            field_dict["source"] = source
        if execution_stage is not UNSET:
            field_dict["execution_stage"] = execution_stage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_execution_relevant_link_create import (
            TestExecutionRelevantLinkCreate,
        )

        d = dict(src_dict)
        name = d.pop("name")

        version = d.pop("version")

        arch = d.pop("arch")

        environment = d.pop("environment")

        test_plan = d.pop("test_plan")

        family = cast(Literal["deb"], d.pop("family"))
        if family != "deb":
            raise ValueError(f"family must match const 'deb', got '{family}'")

        series = d.pop("series")

        repo = d.pop("repo")

        def _parse_ci_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ci_link = _parse_ci_link(d.pop("ci_link", UNSET))

        _initial_status = d.pop("initial_status", UNSET)
        initial_status: TestExecutionStatus | Unset
        if isinstance(_initial_status, Unset):
            initial_status = UNSET
        else:
            initial_status = TestExecutionStatus(_initial_status)

        _relevant_links = d.pop("relevant_links", UNSET)
        relevant_links: list[TestExecutionRelevantLinkCreate] | Unset = UNSET
        if _relevant_links is not UNSET:
            relevant_links = []
            for relevant_links_item_data in _relevant_links:
                relevant_links_item = TestExecutionRelevantLinkCreate.from_dict(
                    relevant_links_item_data
                )

                relevant_links.append(relevant_links_item)

        needs_assignment = d.pop("needs_assignment", UNSET)

        source = d.pop("source", UNSET)

        def _parse_execution_stage(data: object) -> DebStage | Literal[""] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                execution_stage_type_0 = DebStage(data)

                return execution_stage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            execution_stage_type_1 = cast(Literal[""], data)
            if execution_stage_type_1 != "":
                raise ValueError(
                    f"execution_stage_type_1 must match const '', got '{execution_stage_type_1}'"
                )
            return execution_stage_type_1

        execution_stage = _parse_execution_stage(d.pop("execution_stage", UNSET))

        start_deb_test_execution_request = cls(
            name=name,
            version=version,
            arch=arch,
            environment=environment,
            test_plan=test_plan,
            family=family,
            series=series,
            repo=repo,
            ci_link=ci_link,
            initial_status=initial_status,
            relevant_links=relevant_links,
            needs_assignment=needs_assignment,
            source=source,
            execution_stage=execution_stage,
        )

        start_deb_test_execution_request.additional_properties = d
        return start_deb_test_execution_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
