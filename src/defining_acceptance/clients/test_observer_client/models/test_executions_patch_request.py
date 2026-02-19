from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.test_execution_status import TestExecutionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_metadata import ExecutionMetadata


T = TypeVar("T", bound="TestExecutionsPatchRequest")


@_attrs_define
class TestExecutionsPatchRequest:
    """
    Attributes:
        c3_link (None | str | Unset):
        ci_link (None | str | Unset):
        status (Literal['COMPLETED'] | None | TestExecutionStatus | Unset):
        execution_metadata (ExecutionMetadata | None | Unset):
    """

    c3_link: None | str | Unset = UNSET
    ci_link: None | str | Unset = UNSET
    status: Literal["COMPLETED"] | None | TestExecutionStatus | Unset = UNSET
    execution_metadata: ExecutionMetadata | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.execution_metadata import ExecutionMetadata

        c3_link: None | str | Unset
        if isinstance(self.c3_link, Unset):
            c3_link = UNSET
        else:
            c3_link = self.c3_link

        ci_link: None | str | Unset
        if isinstance(self.ci_link, Unset):
            ci_link = UNSET
        else:
            ci_link = self.ci_link

        status: Literal["COMPLETED"] | None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, TestExecutionStatus):
            status = self.status.value
        else:
            status = self.status

        execution_metadata: dict[str, Any] | None | Unset
        if isinstance(self.execution_metadata, Unset):
            execution_metadata = UNSET
        elif isinstance(self.execution_metadata, ExecutionMetadata):
            execution_metadata = self.execution_metadata.to_dict()
        else:
            execution_metadata = self.execution_metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if c3_link is not UNSET:
            field_dict["c3_link"] = c3_link
        if ci_link is not UNSET:
            field_dict["ci_link"] = ci_link
        if status is not UNSET:
            field_dict["status"] = status
        if execution_metadata is not UNSET:
            field_dict["execution_metadata"] = execution_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_metadata import ExecutionMetadata

        d = dict(src_dict)

        def _parse_c3_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        c3_link = _parse_c3_link(d.pop("c3_link", UNSET))

        def _parse_ci_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ci_link = _parse_ci_link(d.pop("ci_link", UNSET))

        def _parse_status(
            data: object,
        ) -> Literal["COMPLETED"] | None | TestExecutionStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = TestExecutionStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            status_type_1 = cast(Literal["COMPLETED"], data)
            if status_type_1 != "COMPLETED":
                raise ValueError(
                    f"status_type_1 must match const 'COMPLETED', got '{status_type_1}'"
                )
            return status_type_1
            return cast(Literal["COMPLETED"] | None | TestExecutionStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_execution_metadata(data: object) -> ExecutionMetadata | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                execution_metadata_type_0 = ExecutionMetadata.from_dict(data)

                return execution_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExecutionMetadata | None | Unset, data)

        execution_metadata = _parse_execution_metadata(
            d.pop("execution_metadata", UNSET)
        )

        test_executions_patch_request = cls(
            c3_link=c3_link,
            ci_link=ci_link,
            status=status,
            execution_metadata=execution_metadata,
        )

        test_executions_patch_request.additional_properties = d
        return test_executions_patch_request

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
