from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.artefact_status import ArtefactStatus
from ..models.stage_name import StageName
from ..types import UNSET, Unset

T = TypeVar("T", bound="ArtefactPatch")


@_attrs_define
class ArtefactPatch:
    """
    Attributes:
        status (ArtefactStatus | None | Unset):
        archived (bool | None | Unset):
        stage (None | StageName | Unset):
        comment (None | str | Unset):
        assignee_id (int | None | Unset):
        assignee_email (None | str | Unset):
    """

    status: ArtefactStatus | None | Unset = UNSET
    archived: bool | None | Unset = UNSET
    stage: None | StageName | Unset = UNSET
    comment: None | str | Unset = UNSET
    assignee_id: int | None | Unset = UNSET
    assignee_email: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, ArtefactStatus):
            status = self.status.value
        else:
            status = self.status

        archived: bool | None | Unset
        if isinstance(self.archived, Unset):
            archived = UNSET
        else:
            archived = self.archived

        stage: None | str | Unset
        if isinstance(self.stage, Unset):
            stage = UNSET
        elif isinstance(self.stage, StageName):
            stage = self.stage.value
        else:
            stage = self.stage

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        assignee_id: int | None | Unset
        if isinstance(self.assignee_id, Unset):
            assignee_id = UNSET
        else:
            assignee_id = self.assignee_id

        assignee_email: None | str | Unset
        if isinstance(self.assignee_email, Unset):
            assignee_email = UNSET
        else:
            assignee_email = self.assignee_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if archived is not UNSET:
            field_dict["archived"] = archived
        if stage is not UNSET:
            field_dict["stage"] = stage
        if comment is not UNSET:
            field_dict["comment"] = comment
        if assignee_id is not UNSET:
            field_dict["assignee_id"] = assignee_id
        if assignee_email is not UNSET:
            field_dict["assignee_email"] = assignee_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_status(data: object) -> ArtefactStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = ArtefactStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ArtefactStatus | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_archived(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        archived = _parse_archived(d.pop("archived", UNSET))

        def _parse_stage(data: object) -> None | StageName | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                stage_type_0 = StageName(data)

                return stage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StageName | Unset, data)

        stage = _parse_stage(d.pop("stage", UNSET))

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_assignee_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        assignee_id = _parse_assignee_id(d.pop("assignee_id", UNSET))

        def _parse_assignee_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assignee_email = _parse_assignee_email(d.pop("assignee_email", UNSET))

        artefact_patch = cls(
            status=status,
            archived=archived,
            stage=stage,
            comment=comment,
            assignee_id=assignee_id,
            assignee_email=assignee_email,
        )

        artefact_patch.additional_properties = d
        return artefact_patch

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
