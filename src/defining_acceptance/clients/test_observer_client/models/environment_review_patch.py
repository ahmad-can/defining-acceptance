from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.artefact_build_environment_review_decision import (
    ArtefactBuildEnvironmentReviewDecision,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvironmentReviewPatch")


@_attrs_define
class EnvironmentReviewPatch:
    """
    Attributes:
        review_decision (list[ArtefactBuildEnvironmentReviewDecision] | None | Unset):
        review_comment (None | str | Unset):
    """

    review_decision: list[ArtefactBuildEnvironmentReviewDecision] | None | Unset = UNSET
    review_comment: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        review_decision: list[str] | None | Unset
        if isinstance(self.review_decision, Unset):
            review_decision = UNSET
        elif isinstance(self.review_decision, list):
            review_decision = []
            for review_decision_type_0_item_data in self.review_decision:
                review_decision_type_0_item = review_decision_type_0_item_data.value
                review_decision.append(review_decision_type_0_item)

        else:
            review_decision = self.review_decision

        review_comment: None | str | Unset
        if isinstance(self.review_comment, Unset):
            review_comment = UNSET
        else:
            review_comment = self.review_comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if review_decision is not UNSET:
            field_dict["review_decision"] = review_decision
        if review_comment is not UNSET:
            field_dict["review_comment"] = review_comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_review_decision(
            data: object,
        ) -> list[ArtefactBuildEnvironmentReviewDecision] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                review_decision_type_0 = []
                _review_decision_type_0 = data
                for review_decision_type_0_item_data in _review_decision_type_0:
                    review_decision_type_0_item = (
                        ArtefactBuildEnvironmentReviewDecision(
                            review_decision_type_0_item_data
                        )
                    )

                    review_decision_type_0.append(review_decision_type_0_item)

                return review_decision_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[ArtefactBuildEnvironmentReviewDecision] | None | Unset, data
            )

        review_decision = _parse_review_decision(d.pop("review_decision", UNSET))

        def _parse_review_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        review_comment = _parse_review_comment(d.pop("review_comment", UNSET))

        environment_review_patch = cls(
            review_decision=review_decision,
            review_comment=review_comment,
        )

        environment_review_patch.additional_properties = d
        return environment_review_patch

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
