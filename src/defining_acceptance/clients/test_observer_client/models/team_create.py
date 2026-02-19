from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.permission import Permission
from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamCreate")


@_attrs_define
class TeamCreate:
    """
    Attributes:
        name (str):
        permissions (list[Permission] | Unset):
        reviewer_families (list[str] | Unset):
    """

    name: str
    permissions: list[Permission] | Unset = UNSET
    reviewer_families: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.value
                permissions.append(permissions_item)

        reviewer_families: list[str] | Unset = UNSET
        if not isinstance(self.reviewer_families, Unset):
            reviewer_families = self.reviewer_families

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if reviewer_families is not UNSET:
            field_dict["reviewer_families"] = reviewer_families

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _permissions = d.pop("permissions", UNSET)
        permissions: list[Permission] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for permissions_item_data in _permissions:
                permissions_item = Permission(permissions_item_data)

                permissions.append(permissions_item)

        reviewer_families = cast(list[str], d.pop("reviewer_families", UNSET))

        team_create = cls(
            name=name,
            permissions=permissions,
            reviewer_families=reviewer_families,
        )

        team_create.additional_properties = d
        return team_create

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
