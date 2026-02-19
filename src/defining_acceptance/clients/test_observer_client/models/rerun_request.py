from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.test_result_search_filters import TestResultSearchFilters


T = TypeVar("T", bound="RerunRequest")


@_attrs_define
class RerunRequest:
    """
    Attributes:
        test_execution_ids (list[int] | Unset):
        test_results_filters (None | TestResultSearchFilters | Unset):
    """

    test_execution_ids: list[int] | Unset = UNSET
    test_results_filters: None | TestResultSearchFilters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.test_result_search_filters import TestResultSearchFilters

        test_execution_ids: list[int] | Unset = UNSET
        if not isinstance(self.test_execution_ids, Unset):
            test_execution_ids = self.test_execution_ids

        test_results_filters: dict[str, Any] | None | Unset
        if isinstance(self.test_results_filters, Unset):
            test_results_filters = UNSET
        elif isinstance(self.test_results_filters, TestResultSearchFilters):
            test_results_filters = self.test_results_filters.to_dict()
        else:
            test_results_filters = self.test_results_filters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if test_execution_ids is not UNSET:
            field_dict["test_execution_ids"] = test_execution_ids
        if test_results_filters is not UNSET:
            field_dict["test_results_filters"] = test_results_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_result_search_filters import TestResultSearchFilters

        d = dict(src_dict)
        test_execution_ids = cast(list[int], d.pop("test_execution_ids", UNSET))

        def _parse_test_results_filters(
            data: object,
        ) -> None | TestResultSearchFilters | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                test_results_filters_type_0 = TestResultSearchFilters.from_dict(data)

                return test_results_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TestResultSearchFilters | Unset, data)

        test_results_filters = _parse_test_results_filters(
            d.pop("test_results_filters", UNSET)
        )

        rerun_request = cls(
            test_execution_ids=test_execution_ids,
            test_results_filters=test_results_filters,
        )

        rerun_request.additional_properties = d
        return rerun_request

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
