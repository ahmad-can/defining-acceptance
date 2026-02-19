from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.family_name import FamilyName
from ..models.test_result_status import TestResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_metadata import ExecutionMetadata


T = TypeVar("T", bound="IssueTestResultAttachmentRulePostRequest")


@_attrs_define
class IssueTestResultAttachmentRulePostRequest:
    """
    Attributes:
        enabled (bool | Unset):  Default: True.
        families (list[FamilyName] | Unset):
        environment_names (list[str] | Unset):
        test_case_names (list[str] | Unset):
        template_ids (list[str] | Unset):
        test_result_statuses (list[TestResultStatus] | Unset):
        execution_metadata (ExecutionMetadata | Unset): A mapping of string categories to lists of string values.
    """

    enabled: bool | Unset = True
    families: list[FamilyName] | Unset = UNSET
    environment_names: list[str] | Unset = UNSET
    test_case_names: list[str] | Unset = UNSET
    template_ids: list[str] | Unset = UNSET
    test_result_statuses: list[TestResultStatus] | Unset = UNSET
    execution_metadata: ExecutionMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        families: list[str] | Unset = UNSET
        if not isinstance(self.families, Unset):
            families = []
            for families_item_data in self.families:
                families_item = families_item_data.value
                families.append(families_item)

        environment_names: list[str] | Unset = UNSET
        if not isinstance(self.environment_names, Unset):
            environment_names = self.environment_names

        test_case_names: list[str] | Unset = UNSET
        if not isinstance(self.test_case_names, Unset):
            test_case_names = self.test_case_names

        template_ids: list[str] | Unset = UNSET
        if not isinstance(self.template_ids, Unset):
            template_ids = self.template_ids

        test_result_statuses: list[str] | Unset = UNSET
        if not isinstance(self.test_result_statuses, Unset):
            test_result_statuses = []
            for test_result_statuses_item_data in self.test_result_statuses:
                test_result_statuses_item = test_result_statuses_item_data.value
                test_result_statuses.append(test_result_statuses_item)

        execution_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_metadata, Unset):
            execution_metadata = self.execution_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if families is not UNSET:
            field_dict["families"] = families
        if environment_names is not UNSET:
            field_dict["environment_names"] = environment_names
        if test_case_names is not UNSET:
            field_dict["test_case_names"] = test_case_names
        if template_ids is not UNSET:
            field_dict["template_ids"] = template_ids
        if test_result_statuses is not UNSET:
            field_dict["test_result_statuses"] = test_result_statuses
        if execution_metadata is not UNSET:
            field_dict["execution_metadata"] = execution_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_metadata import ExecutionMetadata

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _families = d.pop("families", UNSET)
        families: list[FamilyName] | Unset = UNSET
        if _families is not UNSET:
            families = []
            for families_item_data in _families:
                families_item = FamilyName(families_item_data)

                families.append(families_item)

        environment_names = cast(list[str], d.pop("environment_names", UNSET))

        test_case_names = cast(list[str], d.pop("test_case_names", UNSET))

        template_ids = cast(list[str], d.pop("template_ids", UNSET))

        _test_result_statuses = d.pop("test_result_statuses", UNSET)
        test_result_statuses: list[TestResultStatus] | Unset = UNSET
        if _test_result_statuses is not UNSET:
            test_result_statuses = []
            for test_result_statuses_item_data in _test_result_statuses:
                test_result_statuses_item = TestResultStatus(
                    test_result_statuses_item_data
                )

                test_result_statuses.append(test_result_statuses_item)

        _execution_metadata = d.pop("execution_metadata", UNSET)
        execution_metadata: ExecutionMetadata | Unset
        if isinstance(_execution_metadata, Unset):
            execution_metadata = UNSET
        else:
            execution_metadata = ExecutionMetadata.from_dict(_execution_metadata)

        issue_test_result_attachment_rule_post_request = cls(
            enabled=enabled,
            families=families,
            environment_names=environment_names,
            test_case_names=test_case_names,
            template_ids=template_ids,
            test_result_statuses=test_result_statuses,
            execution_metadata=execution_metadata,
        )

        issue_test_result_attachment_rule_post_request.additional_properties = d
        return issue_test_result_attachment_rule_post_request

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
