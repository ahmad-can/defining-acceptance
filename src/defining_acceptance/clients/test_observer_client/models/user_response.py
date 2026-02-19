from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_minimal_response import TeamMinimalResponse


T = TypeVar("T", bound="UserResponse")


@_attrs_define
class UserResponse:
    """
    Attributes:
        id (int):
        email (str):
        name (str):
        teams (list[TeamMinimalResponse]):
        is_admin (bool):
        launchpad_handle (None | str | Unset):
    """

    id: int
    email: str
    name: str
    teams: list[TeamMinimalResponse]
    is_admin: bool
    launchpad_handle: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        name = self.name

        teams = []
        for teams_item_data in self.teams:
            teams_item = teams_item_data.to_dict()
            teams.append(teams_item)

        is_admin = self.is_admin

        launchpad_handle: None | str | Unset
        if isinstance(self.launchpad_handle, Unset):
            launchpad_handle = UNSET
        else:
            launchpad_handle = self.launchpad_handle

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "name": name,
                "teams": teams,
                "is_admin": is_admin,
            }
        )
        if launchpad_handle is not UNSET:
            field_dict["launchpad_handle"] = launchpad_handle

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_minimal_response import TeamMinimalResponse

        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        name = d.pop("name")

        teams = []
        _teams = d.pop("teams")
        for teams_item_data in _teams:
            teams_item = TeamMinimalResponse.from_dict(teams_item_data)

            teams.append(teams_item)

        is_admin = d.pop("is_admin")

        def _parse_launchpad_handle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        launchpad_handle = _parse_launchpad_handle(d.pop("launchpad_handle", UNSET))

        user_response = cls(
            id=id,
            email=email,
            name=name,
            teams=teams,
            is_admin=is_admin,
            launchpad_handle=launchpad_handle,
        )

        user_response.additional_properties = d
        return user_response

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
