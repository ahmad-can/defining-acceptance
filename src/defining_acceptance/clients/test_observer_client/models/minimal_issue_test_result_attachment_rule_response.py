from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.family_name import FamilyName
from ..models.test_result_status import TestResultStatus

if TYPE_CHECKING:
    from ..models.execution_metadata import ExecutionMetadata


T = TypeVar("T", bound="MinimalIssueTestResultAttachmentRuleResponse")


@_attrs_define
class MinimalIssueTestResultAttachmentRuleResponse:
    """
    Attributes:
        id (int):
        enabled (bool):
        families (list[FamilyName]):
        environment_names (list[str]):
        test_case_names (list[str]):
        template_ids (list[str]):
        test_result_statuses (list[TestResultStatus]):
        execution_metadata (ExecutionMetadata): A mapping of string categories to lists of string values.
    """

    id: int
    enabled: bool
    families: list[FamilyName]
    environment_names: list[str]
    test_case_names: list[str]
    template_ids: list[str]
    test_result_statuses: list[TestResultStatus]
    execution_metadata: ExecutionMetadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        enabled = self.enabled

        families = []
        for families_item_data in self.families:
            families_item = families_item_data.value
            families.append(families_item)

        environment_names = self.environment_names

        test_case_names = self.test_case_names

        template_ids = self.template_ids

        test_result_statuses = []
        for test_result_statuses_item_data in self.test_result_statuses:
            test_result_statuses_item = test_result_statuses_item_data.value
            test_result_statuses.append(test_result_statuses_item)

        execution_metadata = self.execution_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "enabled": enabled,
                "families": families,
                "environment_names": environment_names,
                "test_case_names": test_case_names,
                "template_ids": template_ids,
                "test_result_statuses": test_result_statuses,
                "execution_metadata": execution_metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_metadata import ExecutionMetadata

        d = dict(src_dict)
        id = d.pop("id")

        enabled = d.pop("enabled")

        families = []
        _families = d.pop("families")
        for families_item_data in _families:
            families_item = FamilyName(families_item_data)

            families.append(families_item)

        environment_names = cast(list[str], d.pop("environment_names"))

        test_case_names = cast(list[str], d.pop("test_case_names"))

        template_ids = cast(list[str], d.pop("template_ids"))

        test_result_statuses = []
        _test_result_statuses = d.pop("test_result_statuses")
        for test_result_statuses_item_data in _test_result_statuses:
            test_result_statuses_item = TestResultStatus(test_result_statuses_item_data)

            test_result_statuses.append(test_result_statuses_item)

        execution_metadata = ExecutionMetadata.from_dict(d.pop("execution_metadata"))

        minimal_issue_test_result_attachment_rule_response = cls(
            id=id,
            enabled=enabled,
            families=families,
            environment_names=environment_names,
            test_case_names=test_case_names,
            template_ids=template_ids,
            test_result_statuses=test_result_statuses,
            execution_metadata=execution_metadata,
        )

        minimal_issue_test_result_attachment_rule_response.additional_properties = d
        return minimal_issue_test_result_attachment_rule_response

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
