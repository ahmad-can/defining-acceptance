from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.image_stage import ImageStage
from ..models.test_execution_status import TestExecutionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_execution_relevant_link_create import (
        TestExecutionRelevantLinkCreate,
    )


T = TypeVar("T", bound="StartImageTestExecutionRequest")


@_attrs_define
class StartImageTestExecutionRequest:
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
        execution_stage (ImageStage):
        os (str): Operating system of the image. Examples: 'ubuntu', 'ubuntu-core', 'ubuntu-server'
        release (str): OS release codename or version. Examples: 'focal', 'jammy', 'noble', '20.04', '22.04', '24.04'
        sha256 (str): SHA256 checksum hash uniquely identifying this image build. Used to verify image integrity and
            uniqueness.
        owner (str): Team or organization responsible for the image. Examples: 'canonical', 'ubuntu-images', team names
        image_url (str): Direct URL where the image file can be downloaded or accessed. Should be a valid HTTP/HTTPS
            URL.
        ci_link (None | str | Unset): Optional URL linking to the CI job executing these tests. Useful for tracking test
            runs back to their automation source. Can be omitted.
        initial_status (TestExecutionStatus | Unset):
        relevant_links (list[TestExecutionRelevantLinkCreate] | Unset): Optional list of additional URLs related to this
            test execution (e.g., bug reports, documentation, related PRs). Can be omitted or left empty.
        needs_assignment (bool | Unset): Whether the artefact created from this test execution requires assignment of a
            reviewer. Set to true if test results need human review before the artefact can be promoted. Default false means
            no review assignment needed. Default: False.
        family (Literal['image'] | Unset):  Default: 'image'.
    """

    name: str
    version: str
    arch: str
    environment: str
    test_plan: str
    execution_stage: ImageStage
    os: str
    release: str
    sha256: str
    owner: str
    image_url: str
    ci_link: None | str | Unset = UNSET
    initial_status: TestExecutionStatus | Unset = UNSET
    relevant_links: list[TestExecutionRelevantLinkCreate] | Unset = UNSET
    needs_assignment: bool | Unset = False
    family: Literal["image"] | Unset = "image"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        version = self.version

        arch = self.arch

        environment = self.environment

        test_plan = self.test_plan

        execution_stage = self.execution_stage.value

        os = self.os

        release = self.release

        sha256 = self.sha256

        owner = self.owner

        image_url = self.image_url

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

        family = self.family

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "version": version,
                "arch": arch,
                "environment": environment,
                "test_plan": test_plan,
                "execution_stage": execution_stage,
                "os": os,
                "release": release,
                "sha256": sha256,
                "owner": owner,
                "image_url": image_url,
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
        if family is not UNSET:
            field_dict["family"] = family

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

        execution_stage = ImageStage(d.pop("execution_stage"))

        os = d.pop("os")

        release = d.pop("release")

        sha256 = d.pop("sha256")

        owner = d.pop("owner")

        image_url = d.pop("image_url")

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

        family = cast(Literal["image"] | Unset, d.pop("family", UNSET))
        if family != "image" and not isinstance(family, Unset):
            raise ValueError(f"family must match const 'image', got '{family}'")

        start_image_test_execution_request = cls(
            name=name,
            version=version,
            arch=arch,
            environment=environment,
            test_plan=test_plan,
            execution_stage=execution_stage,
            os=os,
            release=release,
            sha256=sha256,
            owner=owner,
            image_url=image_url,
            ci_link=ci_link,
            initial_status=initial_status,
            relevant_links=relevant_links,
            needs_assignment=needs_assignment,
            family=family,
        )

        start_image_test_execution_request.additional_properties = d
        return start_image_test_execution_request

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
