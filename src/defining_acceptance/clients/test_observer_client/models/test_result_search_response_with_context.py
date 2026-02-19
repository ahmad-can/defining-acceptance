from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.test_result_response_with_context import TestResultResponseWithContext


T = TypeVar("T", bound="TestResultSearchResponseWithContext")


@_attrs_define
class TestResultSearchResponseWithContext:
    """Response model for test results search endpoint with full context

    Attributes:
        count (int):
        test_results (list[TestResultResponseWithContext]):
    """

    count: int
    test_results: list[TestResultResponseWithContext]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        test_results = []
        for test_results_item_data in self.test_results:
            test_results_item = test_results_item_data.to_dict()
            test_results.append(test_results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "test_results": test_results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_result_response_with_context import (
            TestResultResponseWithContext,
        )

        d = dict(src_dict)
        count = d.pop("count")

        test_results = []
        _test_results = d.pop("test_results")
        for test_results_item_data in _test_results:
            test_results_item = TestResultResponseWithContext.from_dict(
                test_results_item_data
            )

            test_results.append(test_results_item)

        test_result_search_response_with_context = cls(
            count=count,
            test_results=test_results,
        )

        test_result_search_response_with_context.additional_properties = d
        return test_result_search_response_with_context

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
