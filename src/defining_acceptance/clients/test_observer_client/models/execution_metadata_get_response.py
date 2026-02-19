from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.execution_metadata import ExecutionMetadata


T = TypeVar("T", bound="ExecutionMetadataGetResponse")


@_attrs_define
class ExecutionMetadataGetResponse:
    """
    Attributes:
        execution_metadata (ExecutionMetadata): A mapping of string categories to lists of string values.
    """

    execution_metadata: ExecutionMetadata
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        execution_metadata = self.execution_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "execution_metadata": execution_metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_metadata import ExecutionMetadata

        d = dict(src_dict)
        execution_metadata = ExecutionMetadata.from_dict(d.pop("execution_metadata"))

        execution_metadata_get_response = cls(
            execution_metadata=execution_metadata,
        )

        execution_metadata_get_response.additional_properties = d
        return execution_metadata_get_response

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
