from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_minimal_response import UserMinimalResponse


T = TypeVar("T", bound="TeamResponse")


@_attrs_define
class TeamResponse:
    """
    Attributes:
        id (int):
        name (str):
        permissions (list[str]):
        members (list[UserMinimalResponse]):
        reviewer_families (list[str] | Unset):
    """

    id: int
    name: str
    permissions: list[str]
    members: list[UserMinimalResponse]
    reviewer_families: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        permissions = self.permissions

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        reviewer_families: list[str] | Unset = UNSET
        if not isinstance(self.reviewer_families, Unset):
            reviewer_families = self.reviewer_families

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "permissions": permissions,
                "members": members,
            }
        )
        if reviewer_families is not UNSET:
            field_dict["reviewer_families"] = reviewer_families

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_minimal_response import UserMinimalResponse

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        permissions = cast(list[str], d.pop("permissions"))

        members = []
        _members = d.pop("members")
        for members_item_data in _members:
            members_item = UserMinimalResponse.from_dict(members_item_data)

            members.append(members_item)

        reviewer_families = cast(list[str], d.pop("reviewer_families", UNSET))

        team_response = cls(
            id=id,
            name=name,
            permissions=permissions,
            members=members,
            reviewer_families=reviewer_families,
        )

        team_response.additional_properties = d
        return team_response

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
