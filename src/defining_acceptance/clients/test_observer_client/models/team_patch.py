from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.permission import Permission
from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamPatch")


@_attrs_define
class TeamPatch:
    """
    Attributes:
        permissions (list[Permission] | None | Unset):
        reviewer_families (list[str] | None | Unset):
    """

    permissions: list[Permission] | None | Unset = UNSET
    reviewer_families: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permissions: list[str] | None | Unset
        if isinstance(self.permissions, Unset):
            permissions = UNSET
        elif isinstance(self.permissions, list):
            permissions = []
            for permissions_type_0_item_data in self.permissions:
                permissions_type_0_item = permissions_type_0_item_data.value
                permissions.append(permissions_type_0_item)

        else:
            permissions = self.permissions

        reviewer_families: list[str] | None | Unset
        if isinstance(self.reviewer_families, Unset):
            reviewer_families = UNSET
        elif isinstance(self.reviewer_families, list):
            reviewer_families = self.reviewer_families

        else:
            reviewer_families = self.reviewer_families

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if reviewer_families is not UNSET:
            field_dict["reviewer_families"] = reviewer_families

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_permissions(data: object) -> list[Permission] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                permissions_type_0 = []
                _permissions_type_0 = data
                for permissions_type_0_item_data in _permissions_type_0:
                    permissions_type_0_item = Permission(permissions_type_0_item_data)

                    permissions_type_0.append(permissions_type_0_item)

                return permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Permission] | None | Unset, data)

        permissions = _parse_permissions(d.pop("permissions", UNSET))

        def _parse_reviewer_families(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reviewer_families_type_0 = cast(list[str], data)

                return reviewer_families_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        reviewer_families = _parse_reviewer_families(d.pop("reviewer_families", UNSET))

        team_patch = cls(
            permissions=permissions,
            reviewer_families=reviewer_families,
        )

        team_patch.additional_properties = d
        return team_patch

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
