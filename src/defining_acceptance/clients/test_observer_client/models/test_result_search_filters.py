from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.family_name import FamilyName
from ..models.test_execution_status import TestExecutionStatus
from ..models.test_result_search_filters_assignee_ids_type_1 import (
    TestResultSearchFiltersAssigneeIdsType1,
)
from ..models.test_result_search_filters_issues_type_1 import (
    TestResultSearchFiltersIssuesType1,
)
from ..models.test_result_status import TestResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_metadata import ExecutionMetadata


T = TypeVar("T", bound="TestResultSearchFilters")


@_attrs_define
class TestResultSearchFilters:
    """
    Attributes:
        families (list[FamilyName] | Unset):
        artefacts (list[str] | Unset):
        artefact_is_archived (bool | None | Unset):
        environments (list[str] | Unset):
        test_cases (list[str] | Unset):
        template_ids (list[str] | Unset):
        execution_metadata (ExecutionMetadata | Unset): A mapping of string categories to lists of string values.
        issues (list[int] | TestResultSearchFiltersIssuesType1 | Unset):
        test_result_statuses (list[TestResultStatus] | Unset):
        test_execution_statuses (list[TestExecutionStatus] | Unset):
        assignee_ids (list[int] | TestResultSearchFiltersAssigneeIdsType1 | Unset):
        rerun_is_requested (bool | None | Unset):
        execution_is_latest (bool | None | Unset):
        from_date (datetime.datetime | None | Unset):
        until_date (datetime.datetime | None | Unset):
        offset (int | None | Unset):
        limit (int | None | Unset):
    """

    families: list[FamilyName] | Unset = UNSET
    artefacts: list[str] | Unset = UNSET
    artefact_is_archived: bool | None | Unset = UNSET
    environments: list[str] | Unset = UNSET
    test_cases: list[str] | Unset = UNSET
    template_ids: list[str] | Unset = UNSET
    execution_metadata: ExecutionMetadata | Unset = UNSET
    issues: list[int] | TestResultSearchFiltersIssuesType1 | Unset = UNSET
    test_result_statuses: list[TestResultStatus] | Unset = UNSET
    test_execution_statuses: list[TestExecutionStatus] | Unset = UNSET
    assignee_ids: list[int] | TestResultSearchFiltersAssigneeIdsType1 | Unset = UNSET
    rerun_is_requested: bool | None | Unset = UNSET
    execution_is_latest: bool | None | Unset = UNSET
    from_date: datetime.datetime | None | Unset = UNSET
    until_date: datetime.datetime | None | Unset = UNSET
    offset: int | None | Unset = UNSET
    limit: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        families: list[str] | Unset = UNSET
        if not isinstance(self.families, Unset):
            families = []
            for families_item_data in self.families:
                families_item = families_item_data.value
                families.append(families_item)

        artefacts: list[str] | Unset = UNSET
        if not isinstance(self.artefacts, Unset):
            artefacts = self.artefacts

        artefact_is_archived: bool | None | Unset
        if isinstance(self.artefact_is_archived, Unset):
            artefact_is_archived = UNSET
        else:
            artefact_is_archived = self.artefact_is_archived

        environments: list[str] | Unset = UNSET
        if not isinstance(self.environments, Unset):
            environments = self.environments

        test_cases: list[str] | Unset = UNSET
        if not isinstance(self.test_cases, Unset):
            test_cases = self.test_cases

        template_ids: list[str] | Unset = UNSET
        if not isinstance(self.template_ids, Unset):
            template_ids = self.template_ids

        execution_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_metadata, Unset):
            execution_metadata = self.execution_metadata.to_dict()

        issues: list[int] | str | Unset
        if isinstance(self.issues, Unset):
            issues = UNSET
        elif isinstance(self.issues, list):
            issues = self.issues

        else:
            issues = self.issues.value

        test_result_statuses: list[str] | Unset = UNSET
        if not isinstance(self.test_result_statuses, Unset):
            test_result_statuses = []
            for test_result_statuses_item_data in self.test_result_statuses:
                test_result_statuses_item = test_result_statuses_item_data.value
                test_result_statuses.append(test_result_statuses_item)

        test_execution_statuses: list[str] | Unset = UNSET
        if not isinstance(self.test_execution_statuses, Unset):
            test_execution_statuses = []
            for test_execution_statuses_item_data in self.test_execution_statuses:
                test_execution_statuses_item = test_execution_statuses_item_data.value
                test_execution_statuses.append(test_execution_statuses_item)

        assignee_ids: list[int] | str | Unset
        if isinstance(self.assignee_ids, Unset):
            assignee_ids = UNSET
        elif isinstance(self.assignee_ids, list):
            assignee_ids = self.assignee_ids

        else:
            assignee_ids = self.assignee_ids.value

        rerun_is_requested: bool | None | Unset
        if isinstance(self.rerun_is_requested, Unset):
            rerun_is_requested = UNSET
        else:
            rerun_is_requested = self.rerun_is_requested

        execution_is_latest: bool | None | Unset
        if isinstance(self.execution_is_latest, Unset):
            execution_is_latest = UNSET
        else:
            execution_is_latest = self.execution_is_latest

        from_date: None | str | Unset
        if isinstance(self.from_date, Unset):
            from_date = UNSET
        elif isinstance(self.from_date, datetime.datetime):
            from_date = self.from_date.isoformat()
        else:
            from_date = self.from_date

        until_date: None | str | Unset
        if isinstance(self.until_date, Unset):
            until_date = UNSET
        elif isinstance(self.until_date, datetime.datetime):
            until_date = self.until_date.isoformat()
        else:
            until_date = self.until_date

        offset: int | None | Unset
        if isinstance(self.offset, Unset):
            offset = UNSET
        else:
            offset = self.offset

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if families is not UNSET:
            field_dict["families"] = families
        if artefacts is not UNSET:
            field_dict["artefacts"] = artefacts
        if artefact_is_archived is not UNSET:
            field_dict["artefact_is_archived"] = artefact_is_archived
        if environments is not UNSET:
            field_dict["environments"] = environments
        if test_cases is not UNSET:
            field_dict["test_cases"] = test_cases
        if template_ids is not UNSET:
            field_dict["template_ids"] = template_ids
        if execution_metadata is not UNSET:
            field_dict["execution_metadata"] = execution_metadata
        if issues is not UNSET:
            field_dict["issues"] = issues
        if test_result_statuses is not UNSET:
            field_dict["test_result_statuses"] = test_result_statuses
        if test_execution_statuses is not UNSET:
            field_dict["test_execution_statuses"] = test_execution_statuses
        if assignee_ids is not UNSET:
            field_dict["assignee_ids"] = assignee_ids
        if rerun_is_requested is not UNSET:
            field_dict["rerun_is_requested"] = rerun_is_requested
        if execution_is_latest is not UNSET:
            field_dict["execution_is_latest"] = execution_is_latest
        if from_date is not UNSET:
            field_dict["from_date"] = from_date
        if until_date is not UNSET:
            field_dict["until_date"] = until_date
        if offset is not UNSET:
            field_dict["offset"] = offset
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_metadata import ExecutionMetadata

        d = dict(src_dict)
        _families = d.pop("families", UNSET)
        families: list[FamilyName] | Unset = UNSET
        if _families is not UNSET:
            families = []
            for families_item_data in _families:
                families_item = FamilyName(families_item_data)

                families.append(families_item)

        artefacts = cast(list[str], d.pop("artefacts", UNSET))

        def _parse_artefact_is_archived(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        artefact_is_archived = _parse_artefact_is_archived(
            d.pop("artefact_is_archived", UNSET)
        )

        environments = cast(list[str], d.pop("environments", UNSET))

        test_cases = cast(list[str], d.pop("test_cases", UNSET))

        template_ids = cast(list[str], d.pop("template_ids", UNSET))

        _execution_metadata = d.pop("execution_metadata", UNSET)
        execution_metadata: ExecutionMetadata | Unset
        if isinstance(_execution_metadata, Unset):
            execution_metadata = UNSET
        else:
            execution_metadata = ExecutionMetadata.from_dict(_execution_metadata)

        def _parse_issues(
            data: object,
        ) -> list[int] | TestResultSearchFiltersIssuesType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                issues_type_0 = cast(list[int], data)

                return issues_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            issues_type_1 = TestResultSearchFiltersIssuesType1(data)

            return issues_type_1

        issues = _parse_issues(d.pop("issues", UNSET))

        _test_result_statuses = d.pop("test_result_statuses", UNSET)
        test_result_statuses: list[TestResultStatus] | Unset = UNSET
        if _test_result_statuses is not UNSET:
            test_result_statuses = []
            for test_result_statuses_item_data in _test_result_statuses:
                test_result_statuses_item = TestResultStatus(
                    test_result_statuses_item_data
                )

                test_result_statuses.append(test_result_statuses_item)

        _test_execution_statuses = d.pop("test_execution_statuses", UNSET)
        test_execution_statuses: list[TestExecutionStatus] | Unset = UNSET
        if _test_execution_statuses is not UNSET:
            test_execution_statuses = []
            for test_execution_statuses_item_data in _test_execution_statuses:
                test_execution_statuses_item = TestExecutionStatus(
                    test_execution_statuses_item_data
                )

                test_execution_statuses.append(test_execution_statuses_item)

        def _parse_assignee_ids(
            data: object,
        ) -> list[int] | TestResultSearchFiltersAssigneeIdsType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assignee_ids_type_0 = cast(list[int], data)

                return assignee_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            assignee_ids_type_1 = TestResultSearchFiltersAssigneeIdsType1(data)

            return assignee_ids_type_1

        assignee_ids = _parse_assignee_ids(d.pop("assignee_ids", UNSET))

        def _parse_rerun_is_requested(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        rerun_is_requested = _parse_rerun_is_requested(
            d.pop("rerun_is_requested", UNSET)
        )

        def _parse_execution_is_latest(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        execution_is_latest = _parse_execution_is_latest(
            d.pop("execution_is_latest", UNSET)
        )

        def _parse_from_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_date_type_0 = isoparse(data)

                return from_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        from_date = _parse_from_date(d.pop("from_date", UNSET))

        def _parse_until_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                until_date_type_0 = isoparse(data)

                return until_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        until_date = _parse_until_date(d.pop("until_date", UNSET))

        def _parse_offset(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        offset = _parse_offset(d.pop("offset", UNSET))

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        test_result_search_filters = cls(
            families=families,
            artefacts=artefacts,
            artefact_is_archived=artefact_is_archived,
            environments=environments,
            test_cases=test_cases,
            template_ids=template_ids,
            execution_metadata=execution_metadata,
            issues=issues,
            test_result_statuses=test_result_statuses,
            test_execution_statuses=test_execution_statuses,
            assignee_ids=assignee_ids,
            rerun_is_requested=rerun_is_requested,
            execution_is_latest=execution_is_latest,
            from_date=from_date,
            until_date=until_date,
            offset=offset,
            limit=limit,
        )

        test_result_search_filters.additional_properties = d
        return test_result_search_filters

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
