from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.test_result_status import TestResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.minimal_issue_test_result_attachment_response import (
        MinimalIssueTestResultAttachmentResponse,
    )
    from ..models.previous_test_result import PreviousTestResult


T = TypeVar("T", bound="TestResultResponse")


@_attrs_define
class TestResultResponse:
    """
    Attributes:
        id (int):
        name (str):
        created_at (datetime.datetime):
        category (str):
        template_id (str):
        status (TestResultStatus):
        comment (str):
        io_log (str):
        issues (list[MinimalIssueTestResultAttachmentResponse]):
        previous_results (list[PreviousTestResult] | Unset): The last 10 test results matched with the current test
            execution. The items are sorted in descending order, the first test result is the most recent, while the last
            one is the oldest one.
    """

    id: int
    name: str
    created_at: datetime.datetime
    category: str
    template_id: str
    status: TestResultStatus
    comment: str
    io_log: str
    issues: list[MinimalIssueTestResultAttachmentResponse]
    previous_results: list[PreviousTestResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        created_at = self.created_at.isoformat()

        category = self.category

        template_id = self.template_id

        status = self.status.value

        comment = self.comment

        io_log = self.io_log

        issues = []
        for issues_item_data in self.issues:
            issues_item = issues_item_data.to_dict()
            issues.append(issues_item)

        previous_results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.previous_results, Unset):
            previous_results = []
            for previous_results_item_data in self.previous_results:
                previous_results_item = previous_results_item_data.to_dict()
                previous_results.append(previous_results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "created_at": created_at,
                "category": category,
                "template_id": template_id,
                "status": status,
                "comment": comment,
                "io_log": io_log,
                "issues": issues,
            }
        )
        if previous_results is not UNSET:
            field_dict["previous_results"] = previous_results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.minimal_issue_test_result_attachment_response import (
            MinimalIssueTestResultAttachmentResponse,
        )
        from ..models.previous_test_result import PreviousTestResult

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        created_at = isoparse(d.pop("created_at"))

        category = d.pop("category")

        template_id = d.pop("template_id")

        status = TestResultStatus(d.pop("status"))

        comment = d.pop("comment")

        io_log = d.pop("io_log")

        issues = []
        _issues = d.pop("issues")
        for issues_item_data in _issues:
            issues_item = MinimalIssueTestResultAttachmentResponse.from_dict(
                issues_item_data
            )

            issues.append(issues_item)

        _previous_results = d.pop("previous_results", UNSET)
        previous_results: list[PreviousTestResult] | Unset = UNSET
        if _previous_results is not UNSET:
            previous_results = []
            for previous_results_item_data in _previous_results:
                previous_results_item = PreviousTestResult.from_dict(
                    previous_results_item_data
                )

                previous_results.append(previous_results_item)

        test_result_response = cls(
            id=id,
            name=name,
            created_at=created_at,
            category=category,
            template_id=template_id,
            status=status,
            comment=comment,
            io_log=io_log,
            issues=issues,
            previous_results=previous_results,
        )

        test_result_response.additional_properties = d
        return test_result_response

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
