from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TestCaseInfo")


@_attrs_define
class TestCaseInfo:
    """
    Attributes:
        test_case (str):
        template_id (None | str):
    """

    test_case: str
    template_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        test_case = self.test_case

        template_id: None | str
        template_id = self.template_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "test_case": test_case,
                "template_id": template_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        test_case = d.pop("test_case")

        def _parse_template_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        template_id = _parse_template_id(d.pop("template_id"))

        test_case_info = cls(
            test_case=test_case,
            template_id=template_id,
        )

        test_case_info.additional_properties = d
        return test_case_info

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
