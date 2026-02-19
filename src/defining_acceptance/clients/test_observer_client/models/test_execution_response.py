from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.test_execution_status import TestExecutionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_response import EnvironmentResponse
    from ..models.execution_metadata import ExecutionMetadata
    from ..models.test_execution_relevant_link_response import (
        TestExecutionRelevantLinkResponse,
    )


T = TypeVar("T", bound="TestExecutionResponse")


@_attrs_define
class TestExecutionResponse:
    """
    Attributes:
        id (int):
        ci_link (None | str):
        c3_link (None | str):
        environment (EnvironmentResponse):
        status (TestExecutionStatus):
        test_plan (str):
        created_at (datetime.datetime):
        execution_metadata (ExecutionMetadata): A mapping of string categories to lists of string values.
        is_triaged (bool):
        is_rerun_requested (bool):
        relevant_links (list[TestExecutionRelevantLinkResponse] | Unset):
    """

    id: int
    ci_link: None | str
    c3_link: None | str
    environment: EnvironmentResponse
    status: TestExecutionStatus
    test_plan: str
    created_at: datetime.datetime
    execution_metadata: ExecutionMetadata
    is_triaged: bool
    is_rerun_requested: bool
    relevant_links: list[TestExecutionRelevantLinkResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ci_link: None | str
        ci_link = self.ci_link

        c3_link: None | str
        c3_link = self.c3_link

        environment = self.environment.to_dict()

        status = self.status.value

        test_plan = self.test_plan

        created_at = self.created_at.isoformat()

        execution_metadata = self.execution_metadata.to_dict()

        is_triaged = self.is_triaged

        is_rerun_requested = self.is_rerun_requested

        relevant_links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.relevant_links, Unset):
            relevant_links = []
            for relevant_links_item_data in self.relevant_links:
                relevant_links_item = relevant_links_item_data.to_dict()
                relevant_links.append(relevant_links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ci_link": ci_link,
                "c3_link": c3_link,
                "environment": environment,
                "status": status,
                "test_plan": test_plan,
                "created_at": created_at,
                "execution_metadata": execution_metadata,
                "is_triaged": is_triaged,
                "is_rerun_requested": is_rerun_requested,
            }
        )
        if relevant_links is not UNSET:
            field_dict["relevant_links"] = relevant_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_response import EnvironmentResponse
        from ..models.execution_metadata import ExecutionMetadata
        from ..models.test_execution_relevant_link_response import (
            TestExecutionRelevantLinkResponse,
        )

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_ci_link(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ci_link = _parse_ci_link(d.pop("ci_link"))

        def _parse_c3_link(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        c3_link = _parse_c3_link(d.pop("c3_link"))

        environment = EnvironmentResponse.from_dict(d.pop("environment"))

        status = TestExecutionStatus(d.pop("status"))

        test_plan = d.pop("test_plan")

        created_at = isoparse(d.pop("created_at"))

        execution_metadata = ExecutionMetadata.from_dict(d.pop("execution_metadata"))

        is_triaged = d.pop("is_triaged")

        is_rerun_requested = d.pop("is_rerun_requested")

        _relevant_links = d.pop("relevant_links", UNSET)
        relevant_links: list[TestExecutionRelevantLinkResponse] | Unset = UNSET
        if _relevant_links is not UNSET:
            relevant_links = []
            for relevant_links_item_data in _relevant_links:
                relevant_links_item = TestExecutionRelevantLinkResponse.from_dict(
                    relevant_links_item_data
                )

                relevant_links.append(relevant_links_item)

        test_execution_response = cls(
            id=id,
            ci_link=ci_link,
            c3_link=c3_link,
            environment=environment,
            status=status,
            test_plan=test_plan,
            created_at=created_at,
            execution_metadata=execution_metadata,
            is_triaged=is_triaged,
            is_rerun_requested=is_rerun_requested,
            relevant_links=relevant_links,
        )

        test_execution_response.additional_properties = d
        return test_execution_response

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
