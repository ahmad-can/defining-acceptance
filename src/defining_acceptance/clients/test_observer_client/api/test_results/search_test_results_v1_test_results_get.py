import datetime
from http import HTTPStatus
from typing import Any, Literal

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.family_name import FamilyName
from ...models.http_validation_error import HTTPValidationError
from ...models.test_execution_status import TestExecutionStatus
from ...models.test_result_search_response_with_context import (
    TestResultSearchResponseWithContext,
)
from ...models.test_result_status import TestResultStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    families: list[FamilyName] | None | Unset = UNSET,
    artefacts: list[str] | None | Unset = UNSET,
    artefact_is_archived: bool | None | Unset = UNSET,
    environments: list[str] | None | Unset = UNSET,
    test_cases: list[str] | None | Unset = UNSET,
    template_ids: list[str] | None | Unset = UNSET,
    issues: list[int]
    | list[Literal["any"]]
    | list[Literal["none"]]
    | None
    | Unset = UNSET,
    test_result_statuses: list[TestResultStatus] | None | Unset = UNSET,
    test_execution_statuses: list[TestExecutionStatus] | None | Unset = UNSET,
    assignee_ids: list[int]
    | list[Literal["any"]]
    | list[Literal["none"]]
    | None
    | Unset = UNSET,
    rerun_is_requested: bool | None | Unset = UNSET,
    execution_is_latest: bool | None | Unset = UNSET,
    from_date: datetime.datetime | None | Unset = UNSET,
    until_date: datetime.datetime | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    execution_metadata: list[str] | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_families: list[str] | None | Unset
    if isinstance(families, Unset):
        json_families = UNSET
    elif isinstance(families, list):
        json_families = []
        for families_type_0_item_data in families:
            families_type_0_item = families_type_0_item_data.value
            json_families.append(families_type_0_item)

    else:
        json_families = families
    params["families"] = json_families

    json_artefacts: list[str] | None | Unset
    if isinstance(artefacts, Unset):
        json_artefacts = UNSET
    elif isinstance(artefacts, list):
        json_artefacts = artefacts

    else:
        json_artefacts = artefacts
    params["artefacts"] = json_artefacts

    json_artefact_is_archived: bool | None | Unset
    if isinstance(artefact_is_archived, Unset):
        json_artefact_is_archived = UNSET
    else:
        json_artefact_is_archived = artefact_is_archived
    params["artefact_is_archived"] = json_artefact_is_archived

    json_environments: list[str] | None | Unset
    if isinstance(environments, Unset):
        json_environments = UNSET
    elif isinstance(environments, list):
        json_environments = environments

    else:
        json_environments = environments
    params["environments"] = json_environments

    json_test_cases: list[str] | None | Unset
    if isinstance(test_cases, Unset):
        json_test_cases = UNSET
    elif isinstance(test_cases, list):
        json_test_cases = test_cases

    else:
        json_test_cases = test_cases
    params["test_cases"] = json_test_cases

    json_template_ids: list[str] | None | Unset
    if isinstance(template_ids, Unset):
        json_template_ids = UNSET
    elif isinstance(template_ids, list):
        json_template_ids = template_ids

    else:
        json_template_ids = template_ids
    params["template_ids"] = json_template_ids

    json_issues: list[int] | list[Literal["any"]] | list[Literal["none"]] | None | Unset
    if isinstance(issues, Unset):
        json_issues = UNSET
    elif isinstance(issues, list):
        json_issues = issues

    elif isinstance(issues, list):
        json_issues = issues

    elif isinstance(issues, list):
        json_issues = issues

    else:
        json_issues = issues
    params["issues"] = json_issues

    json_test_result_statuses: list[str] | None | Unset
    if isinstance(test_result_statuses, Unset):
        json_test_result_statuses = UNSET
    elif isinstance(test_result_statuses, list):
        json_test_result_statuses = []
        for test_result_statuses_type_0_item_data in test_result_statuses:
            test_result_statuses_type_0_item = (
                test_result_statuses_type_0_item_data.value
            )
            json_test_result_statuses.append(test_result_statuses_type_0_item)

    else:
        json_test_result_statuses = test_result_statuses
    params["test_result_statuses"] = json_test_result_statuses

    json_test_execution_statuses: list[str] | None | Unset
    if isinstance(test_execution_statuses, Unset):
        json_test_execution_statuses = UNSET
    elif isinstance(test_execution_statuses, list):
        json_test_execution_statuses = []
        for test_execution_statuses_type_0_item_data in test_execution_statuses:
            test_execution_statuses_type_0_item = (
                test_execution_statuses_type_0_item_data.value
            )
            json_test_execution_statuses.append(test_execution_statuses_type_0_item)

    else:
        json_test_execution_statuses = test_execution_statuses
    params["test_execution_statuses"] = json_test_execution_statuses

    json_assignee_ids: (
        list[int] | list[Literal["any"]] | list[Literal["none"]] | None | Unset
    )
    if isinstance(assignee_ids, Unset):
        json_assignee_ids = UNSET
    elif isinstance(assignee_ids, list):
        json_assignee_ids = assignee_ids

    elif isinstance(assignee_ids, list):
        json_assignee_ids = assignee_ids

    elif isinstance(assignee_ids, list):
        json_assignee_ids = assignee_ids

    else:
        json_assignee_ids = assignee_ids
    params["assignee_ids"] = json_assignee_ids

    json_rerun_is_requested: bool | None | Unset
    if isinstance(rerun_is_requested, Unset):
        json_rerun_is_requested = UNSET
    else:
        json_rerun_is_requested = rerun_is_requested
    params["rerun_is_requested"] = json_rerun_is_requested

    json_execution_is_latest: bool | None | Unset
    if isinstance(execution_is_latest, Unset):
        json_execution_is_latest = UNSET
    else:
        json_execution_is_latest = execution_is_latest
    params["execution_is_latest"] = json_execution_is_latest

    json_from_date: None | str | Unset
    if isinstance(from_date, Unset):
        json_from_date = UNSET
    elif isinstance(from_date, datetime.datetime):
        json_from_date = from_date.isoformat()
    else:
        json_from_date = from_date
    params["from_date"] = json_from_date

    json_until_date: None | str | Unset
    if isinstance(until_date, Unset):
        json_until_date = UNSET
    elif isinstance(until_date, datetime.datetime):
        json_until_date = until_date.isoformat()
    else:
        json_until_date = until_date
    params["until_date"] = json_until_date

    params["limit"] = limit

    params["offset"] = offset

    json_execution_metadata: list[str] | None | Unset
    if isinstance(execution_metadata, Unset):
        json_execution_metadata = UNSET
    elif isinstance(execution_metadata, list):
        json_execution_metadata = execution_metadata

    else:
        json_execution_metadata = execution_metadata
    params["execution_metadata"] = json_execution_metadata

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/test-results",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TestResultSearchResponseWithContext | None:
    if response.status_code == 200:
        response_200 = TestResultSearchResponseWithContext.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | TestResultSearchResponseWithContext]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    families: list[FamilyName] | None | Unset = UNSET,
    artefacts: list[str] | None | Unset = UNSET,
    artefact_is_archived: bool | None | Unset = UNSET,
    environments: list[str] | None | Unset = UNSET,
    test_cases: list[str] | None | Unset = UNSET,
    template_ids: list[str] | None | Unset = UNSET,
    issues: list[int]
    | list[Literal["any"]]
    | list[Literal["none"]]
    | None
    | Unset = UNSET,
    test_result_statuses: list[TestResultStatus] | None | Unset = UNSET,
    test_execution_statuses: list[TestExecutionStatus] | None | Unset = UNSET,
    assignee_ids: list[int]
    | list[Literal["any"]]
    | list[Literal["none"]]
    | None
    | Unset = UNSET,
    rerun_is_requested: bool | None | Unset = UNSET,
    execution_is_latest: bool | None | Unset = UNSET,
    from_date: datetime.datetime | None | Unset = UNSET,
    until_date: datetime.datetime | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    execution_metadata: list[str] | None | Unset = UNSET,
) -> Response[HTTPValidationError | TestResultSearchResponseWithContext]:
    """Search Test Results

     Search test results across artefacts using flexible filters.

    This endpoint uses a single optimized query with window functions to get both
    the total count and paginated results in one database round trip.

    Args:
        families (list[FamilyName] | None | Unset): Filter by artefact families (e.g., charm,snap)
        artefacts (list[str] | None | Unset): Filter by artefact names
        artefact_is_archived (bool | None | Unset): Filter by whether the artefact is archived
        environments (list[str] | None | Unset): Filter by environment names
        test_cases (list[str] | None | Unset): Filter by test case names
        template_ids (list[str] | None | Unset): Filter by template IDs
        issues (list[int] | list[Literal['any']] | list[Literal['none']] | None | Unset): Filter
            by issue IDs
        test_result_statuses (list[TestResultStatus] | None | Unset): Filter by test result
            statuses
        test_execution_statuses (list[TestExecutionStatus] | None | Unset): Filter by test
            execution statuses
        assignee_ids (list[int] | list[Literal['any']] | list[Literal['none']] | None | Unset):
            Filter by assignee user ids
        rerun_is_requested (bool | None | Unset): Filter by whether a rerun has been requested for
            the test execution
        execution_is_latest (bool | None | Unset): Filter by whether the test execution is the
            latest in its environment/artifact/test plan combination
        from_date (datetime.datetime | None | Unset): Filter results from this timestamp
        until_date (datetime.datetime | None | Unset): Filter results until this timestamp
        limit (int | Unset): Maximum number of results to return Default: 50.
        offset (int | Unset): Number of results to skip for pagination Default: 0.
        execution_metadata (list[str] | None | Unset): Filter by execution metadata (base64
            encoded category:value pairs).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TestResultSearchResponseWithContext]
    """

    kwargs = _get_kwargs(
        families=families,
        artefacts=artefacts,
        artefact_is_archived=artefact_is_archived,
        environments=environments,
        test_cases=test_cases,
        template_ids=template_ids,
        issues=issues,
        test_result_statuses=test_result_statuses,
        test_execution_statuses=test_execution_statuses,
        assignee_ids=assignee_ids,
        rerun_is_requested=rerun_is_requested,
        execution_is_latest=execution_is_latest,
        from_date=from_date,
        until_date=until_date,
        limit=limit,
        offset=offset,
        execution_metadata=execution_metadata,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    families: list[FamilyName] | None | Unset = UNSET,
    artefacts: list[str] | None | Unset = UNSET,
    artefact_is_archived: bool | None | Unset = UNSET,
    environments: list[str] | None | Unset = UNSET,
    test_cases: list[str] | None | Unset = UNSET,
    template_ids: list[str] | None | Unset = UNSET,
    issues: list[int]
    | list[Literal["any"]]
    | list[Literal["none"]]
    | None
    | Unset = UNSET,
    test_result_statuses: list[TestResultStatus] | None | Unset = UNSET,
    test_execution_statuses: list[TestExecutionStatus] | None | Unset = UNSET,
    assignee_ids: list[int]
    | list[Literal["any"]]
    | list[Literal["none"]]
    | None
    | Unset = UNSET,
    rerun_is_requested: bool | None | Unset = UNSET,
    execution_is_latest: bool | None | Unset = UNSET,
    from_date: datetime.datetime | None | Unset = UNSET,
    until_date: datetime.datetime | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    execution_metadata: list[str] | None | Unset = UNSET,
) -> HTTPValidationError | TestResultSearchResponseWithContext | None:
    """Search Test Results

     Search test results across artefacts using flexible filters.

    This endpoint uses a single optimized query with window functions to get both
    the total count and paginated results in one database round trip.

    Args:
        families (list[FamilyName] | None | Unset): Filter by artefact families (e.g., charm,snap)
        artefacts (list[str] | None | Unset): Filter by artefact names
        artefact_is_archived (bool | None | Unset): Filter by whether the artefact is archived
        environments (list[str] | None | Unset): Filter by environment names
        test_cases (list[str] | None | Unset): Filter by test case names
        template_ids (list[str] | None | Unset): Filter by template IDs
        issues (list[int] | list[Literal['any']] | list[Literal['none']] | None | Unset): Filter
            by issue IDs
        test_result_statuses (list[TestResultStatus] | None | Unset): Filter by test result
            statuses
        test_execution_statuses (list[TestExecutionStatus] | None | Unset): Filter by test
            execution statuses
        assignee_ids (list[int] | list[Literal['any']] | list[Literal['none']] | None | Unset):
            Filter by assignee user ids
        rerun_is_requested (bool | None | Unset): Filter by whether a rerun has been requested for
            the test execution
        execution_is_latest (bool | None | Unset): Filter by whether the test execution is the
            latest in its environment/artifact/test plan combination
        from_date (datetime.datetime | None | Unset): Filter results from this timestamp
        until_date (datetime.datetime | None | Unset): Filter results until this timestamp
        limit (int | Unset): Maximum number of results to return Default: 50.
        offset (int | Unset): Number of results to skip for pagination Default: 0.
        execution_metadata (list[str] | None | Unset): Filter by execution metadata (base64
            encoded category:value pairs).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TestResultSearchResponseWithContext
    """

    return sync_detailed(
        client=client,
        families=families,
        artefacts=artefacts,
        artefact_is_archived=artefact_is_archived,
        environments=environments,
        test_cases=test_cases,
        template_ids=template_ids,
        issues=issues,
        test_result_statuses=test_result_statuses,
        test_execution_statuses=test_execution_statuses,
        assignee_ids=assignee_ids,
        rerun_is_requested=rerun_is_requested,
        execution_is_latest=execution_is_latest,
        from_date=from_date,
        until_date=until_date,
        limit=limit,
        offset=offset,
        execution_metadata=execution_metadata,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    families: list[FamilyName] | None | Unset = UNSET,
    artefacts: list[str] | None | Unset = UNSET,
    artefact_is_archived: bool | None | Unset = UNSET,
    environments: list[str] | None | Unset = UNSET,
    test_cases: list[str] | None | Unset = UNSET,
    template_ids: list[str] | None | Unset = UNSET,
    issues: list[int]
    | list[Literal["any"]]
    | list[Literal["none"]]
    | None
    | Unset = UNSET,
    test_result_statuses: list[TestResultStatus] | None | Unset = UNSET,
    test_execution_statuses: list[TestExecutionStatus] | None | Unset = UNSET,
    assignee_ids: list[int]
    | list[Literal["any"]]
    | list[Literal["none"]]
    | None
    | Unset = UNSET,
    rerun_is_requested: bool | None | Unset = UNSET,
    execution_is_latest: bool | None | Unset = UNSET,
    from_date: datetime.datetime | None | Unset = UNSET,
    until_date: datetime.datetime | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    execution_metadata: list[str] | None | Unset = UNSET,
) -> Response[HTTPValidationError | TestResultSearchResponseWithContext]:
    """Search Test Results

     Search test results across artefacts using flexible filters.

    This endpoint uses a single optimized query with window functions to get both
    the total count and paginated results in one database round trip.

    Args:
        families (list[FamilyName] | None | Unset): Filter by artefact families (e.g., charm,snap)
        artefacts (list[str] | None | Unset): Filter by artefact names
        artefact_is_archived (bool | None | Unset): Filter by whether the artefact is archived
        environments (list[str] | None | Unset): Filter by environment names
        test_cases (list[str] | None | Unset): Filter by test case names
        template_ids (list[str] | None | Unset): Filter by template IDs
        issues (list[int] | list[Literal['any']] | list[Literal['none']] | None | Unset): Filter
            by issue IDs
        test_result_statuses (list[TestResultStatus] | None | Unset): Filter by test result
            statuses
        test_execution_statuses (list[TestExecutionStatus] | None | Unset): Filter by test
            execution statuses
        assignee_ids (list[int] | list[Literal['any']] | list[Literal['none']] | None | Unset):
            Filter by assignee user ids
        rerun_is_requested (bool | None | Unset): Filter by whether a rerun has been requested for
            the test execution
        execution_is_latest (bool | None | Unset): Filter by whether the test execution is the
            latest in its environment/artifact/test plan combination
        from_date (datetime.datetime | None | Unset): Filter results from this timestamp
        until_date (datetime.datetime | None | Unset): Filter results until this timestamp
        limit (int | Unset): Maximum number of results to return Default: 50.
        offset (int | Unset): Number of results to skip for pagination Default: 0.
        execution_metadata (list[str] | None | Unset): Filter by execution metadata (base64
            encoded category:value pairs).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TestResultSearchResponseWithContext]
    """

    kwargs = _get_kwargs(
        families=families,
        artefacts=artefacts,
        artefact_is_archived=artefact_is_archived,
        environments=environments,
        test_cases=test_cases,
        template_ids=template_ids,
        issues=issues,
        test_result_statuses=test_result_statuses,
        test_execution_statuses=test_execution_statuses,
        assignee_ids=assignee_ids,
        rerun_is_requested=rerun_is_requested,
        execution_is_latest=execution_is_latest,
        from_date=from_date,
        until_date=until_date,
        limit=limit,
        offset=offset,
        execution_metadata=execution_metadata,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    families: list[FamilyName] | None | Unset = UNSET,
    artefacts: list[str] | None | Unset = UNSET,
    artefact_is_archived: bool | None | Unset = UNSET,
    environments: list[str] | None | Unset = UNSET,
    test_cases: list[str] | None | Unset = UNSET,
    template_ids: list[str] | None | Unset = UNSET,
    issues: list[int]
    | list[Literal["any"]]
    | list[Literal["none"]]
    | None
    | Unset = UNSET,
    test_result_statuses: list[TestResultStatus] | None | Unset = UNSET,
    test_execution_statuses: list[TestExecutionStatus] | None | Unset = UNSET,
    assignee_ids: list[int]
    | list[Literal["any"]]
    | list[Literal["none"]]
    | None
    | Unset = UNSET,
    rerun_is_requested: bool | None | Unset = UNSET,
    execution_is_latest: bool | None | Unset = UNSET,
    from_date: datetime.datetime | None | Unset = UNSET,
    until_date: datetime.datetime | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    execution_metadata: list[str] | None | Unset = UNSET,
) -> HTTPValidationError | TestResultSearchResponseWithContext | None:
    """Search Test Results

     Search test results across artefacts using flexible filters.

    This endpoint uses a single optimized query with window functions to get both
    the total count and paginated results in one database round trip.

    Args:
        families (list[FamilyName] | None | Unset): Filter by artefact families (e.g., charm,snap)
        artefacts (list[str] | None | Unset): Filter by artefact names
        artefact_is_archived (bool | None | Unset): Filter by whether the artefact is archived
        environments (list[str] | None | Unset): Filter by environment names
        test_cases (list[str] | None | Unset): Filter by test case names
        template_ids (list[str] | None | Unset): Filter by template IDs
        issues (list[int] | list[Literal['any']] | list[Literal['none']] | None | Unset): Filter
            by issue IDs
        test_result_statuses (list[TestResultStatus] | None | Unset): Filter by test result
            statuses
        test_execution_statuses (list[TestExecutionStatus] | None | Unset): Filter by test
            execution statuses
        assignee_ids (list[int] | list[Literal['any']] | list[Literal['none']] | None | Unset):
            Filter by assignee user ids
        rerun_is_requested (bool | None | Unset): Filter by whether a rerun has been requested for
            the test execution
        execution_is_latest (bool | None | Unset): Filter by whether the test execution is the
            latest in its environment/artifact/test plan combination
        from_date (datetime.datetime | None | Unset): Filter results from this timestamp
        until_date (datetime.datetime | None | Unset): Filter results until this timestamp
        limit (int | Unset): Maximum number of results to return Default: 50.
        offset (int | Unset): Number of results to skip for pagination Default: 0.
        execution_metadata (list[str] | None | Unset): Filter by execution metadata (base64
            encoded category:value pairs).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TestResultSearchResponseWithContext
    """

    return (
        await asyncio_detailed(
            client=client,
            families=families,
            artefacts=artefacts,
            artefact_is_archived=artefact_is_archived,
            environments=environments,
            test_cases=test_cases,
            template_ids=template_ids,
            issues=issues,
            test_result_statuses=test_result_statuses,
            test_execution_statuses=test_execution_statuses,
            assignee_ids=assignee_ids,
            rerun_is_requested=rerun_is_requested,
            execution_is_latest=execution_is_latest,
            from_date=from_date,
            until_date=until_date,
            limit=limit,
            offset=offset,
            execution_metadata=execution_metadata,
        )
    ).parsed
