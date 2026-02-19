from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.test_case_info import TestCaseInfo


T = TypeVar("T", bound="TestCasesResponse")


@_attrs_define
class TestCasesResponse:
    """
    Attributes:
        test_cases (list[TestCaseInfo]):
    """

    test_cases: list[TestCaseInfo]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        test_cases = []
        for test_cases_item_data in self.test_cases:
            test_cases_item = test_cases_item_data.to_dict()
            test_cases.append(test_cases_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "test_cases": test_cases,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_case_info import TestCaseInfo

        d = dict(src_dict)
        test_cases = []
        _test_cases = d.pop("test_cases")
        for test_cases_item_data in _test_cases:
            test_cases_item = TestCaseInfo.from_dict(test_cases_item_data)

            test_cases.append(test_cases_item)

        test_cases_response = cls(
            test_cases=test_cases,
        )

        test_cases_response.additional_properties = d
        return test_cases_response

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
