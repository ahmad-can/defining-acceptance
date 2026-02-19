from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.artefact_build_minimal_response import ArtefactBuildMinimalResponse
    from ..models.artefact_response import ArtefactResponse
    from ..models.test_execution_response import TestExecutionResponse
    from ..models.test_result_response import TestResultResponse


T = TypeVar("T", bound="TestResultResponseWithContext")


@_attrs_define
class TestResultResponseWithContext:
    """Test result response with artefact and test execution context

    Attributes:
        test_result (TestResultResponse):
        test_execution (TestExecutionResponse):
        artefact (ArtefactResponse):
        artefact_build (ArtefactBuildMinimalResponse):
    """

    test_result: TestResultResponse
    test_execution: TestExecutionResponse
    artefact: ArtefactResponse
    artefact_build: ArtefactBuildMinimalResponse
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        test_result = self.test_result.to_dict()

        test_execution = self.test_execution.to_dict()

        artefact = self.artefact.to_dict()

        artefact_build = self.artefact_build.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "test_result": test_result,
                "test_execution": test_execution,
                "artefact": artefact,
                "artefact_build": artefact_build,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.artefact_build_minimal_response import (
            ArtefactBuildMinimalResponse,
        )
        from ..models.artefact_response import ArtefactResponse
        from ..models.test_execution_response import TestExecutionResponse
        from ..models.test_result_response import TestResultResponse

        d = dict(src_dict)
        test_result = TestResultResponse.from_dict(d.pop("test_result"))

        test_execution = TestExecutionResponse.from_dict(d.pop("test_execution"))

        artefact = ArtefactResponse.from_dict(d.pop("artefact"))

        artefact_build = ArtefactBuildMinimalResponse.from_dict(d.pop("artefact_build"))

        test_result_response_with_context = cls(
            test_result=test_result,
            test_execution=test_execution,
            artefact=artefact,
            artefact_build=artefact_build,
        )

        test_result_response_with_context.additional_properties = d
        return test_result_response_with_context

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
