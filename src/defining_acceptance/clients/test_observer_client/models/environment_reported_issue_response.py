from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="EnvironmentReportedIssueResponse")


@_attrs_define
class EnvironmentReportedIssueResponse:
    """
    Attributes:
        id (int):
        environment_name (str):
        description (str):
        url (None | str):
        is_confirmed (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: int
    environment_name: str
    description: str
    url: None | str
    is_confirmed: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        environment_name = self.environment_name

        description = self.description

        url: None | str
        url = self.url

        is_confirmed = self.is_confirmed

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "environment_name": environment_name,
                "description": description,
                "url": url,
                "is_confirmed": is_confirmed,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        environment_name = d.pop("environment_name")

        description = d.pop("description")

        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(d.pop("url"))

        is_confirmed = d.pop("is_confirmed")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        environment_reported_issue_response = cls(
            id=id,
            environment_name=environment_name,
            description=description,
            url=url,
            is_confirmed=is_confirmed,
            created_at=created_at,
            updated_at=updated_at,
        )

        environment_reported_issue_response.additional_properties = d
        return environment_reported_issue_response

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
