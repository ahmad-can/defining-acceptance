from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.issue_source import IssueSource
from ..models.issue_status import IssueStatus

T = TypeVar("T", bound="MinimalIssueResponse")


@_attrs_define
class MinimalIssueResponse:
    """
    Attributes:
        id (int):
        source (IssueSource):
        project (str):
        key (str):
        title (str):
        status (IssueStatus):
        url (str):
    """

    id: int
    source: IssueSource
    project: str
    key: str
    title: str
    status: IssueStatus
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        source = self.source.value

        project = self.project

        key = self.key

        title = self.title

        status = self.status.value

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "source": source,
                "project": project,
                "key": key,
                "title": title,
                "status": status,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        source = IssueSource(d.pop("source"))

        project = d.pop("project")

        key = d.pop("key")

        title = d.pop("title")

        status = IssueStatus(d.pop("status"))

        url = d.pop("url")

        minimal_issue_response = cls(
            id=id,
            source=source,
            project=project,
            key=key,
            title=title,
            status=status,
            url=url,
        )

        minimal_issue_response.additional_properties = d
        return minimal_issue_response

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
