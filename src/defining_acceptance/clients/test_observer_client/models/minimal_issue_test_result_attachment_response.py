from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.minimal_issue_response import MinimalIssueResponse
    from ..models.minimal_issue_test_result_attachment_rule_response import (
        MinimalIssueTestResultAttachmentRuleResponse,
    )


T = TypeVar("T", bound="MinimalIssueTestResultAttachmentResponse")


@_attrs_define
class MinimalIssueTestResultAttachmentResponse:
    """
    Attributes:
        issue (MinimalIssueResponse):
        attachment_rule (MinimalIssueTestResultAttachmentRuleResponse | None):
    """

    issue: MinimalIssueResponse
    attachment_rule: MinimalIssueTestResultAttachmentRuleResponse | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.minimal_issue_test_result_attachment_rule_response import (
            MinimalIssueTestResultAttachmentRuleResponse,
        )

        issue = self.issue.to_dict()

        attachment_rule: dict[str, Any] | None
        if isinstance(
            self.attachment_rule, MinimalIssueTestResultAttachmentRuleResponse
        ):
            attachment_rule = self.attachment_rule.to_dict()
        else:
            attachment_rule = self.attachment_rule

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issue": issue,
                "attachment_rule": attachment_rule,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.minimal_issue_response import MinimalIssueResponse
        from ..models.minimal_issue_test_result_attachment_rule_response import (
            MinimalIssueTestResultAttachmentRuleResponse,
        )

        d = dict(src_dict)
        issue = MinimalIssueResponse.from_dict(d.pop("issue"))

        def _parse_attachment_rule(
            data: object,
        ) -> MinimalIssueTestResultAttachmentRuleResponse | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                attachment_rule_type_0 = (
                    MinimalIssueTestResultAttachmentRuleResponse.from_dict(data)
                )

                return attachment_rule_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MinimalIssueTestResultAttachmentRuleResponse | None, data)

        attachment_rule = _parse_attachment_rule(d.pop("attachment_rule"))

        minimal_issue_test_result_attachment_response = cls(
            issue=issue,
            attachment_rule=attachment_rule,
        )

        minimal_issue_test_result_attachment_response.additional_properties = d
        return minimal_issue_test_result_attachment_response

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
