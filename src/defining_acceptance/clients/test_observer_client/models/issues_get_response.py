from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.minimal_issue_response import MinimalIssueResponse


T = TypeVar("T", bound="IssuesGetResponse")


@_attrs_define
class IssuesGetResponse:
    """
    Attributes:
        issues (list[MinimalIssueResponse]):
    """

    issues: list[MinimalIssueResponse]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issues = []
        for issues_item_data in self.issues:
            issues_item = issues_item_data.to_dict()
            issues.append(issues_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issues": issues,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.minimal_issue_response import MinimalIssueResponse

        d = dict(src_dict)
        issues = []
        _issues = d.pop("issues")
        for issues_item_data in _issues:
            issues_item = MinimalIssueResponse.from_dict(issues_item_data)

            issues.append(issues_item)

        issues_get_response = cls(
            issues=issues,
        )

        issues_get_response.additional_properties = d
        return issues_get_response

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
