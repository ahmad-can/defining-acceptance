from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.issue_source import IssueSource
from ...models.issue_status import IssueStatus
from ...models.issues_get_response import IssuesGetResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    source: IssueSource | None | Unset = UNSET,
    project: None | str | Unset = UNSET,
    status: IssueStatus | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    q: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_source: None | str | Unset
    if isinstance(source, Unset):
        json_source = UNSET
    elif isinstance(source, IssueSource):
        json_source = source.value
    else:
        json_source = source
    params["source"] = json_source

    json_project: None | str | Unset
    if isinstance(project, Unset):
        json_project = UNSET
    else:
        json_project = project
    params["project"] = json_project

    json_status: None | str | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, IssueStatus):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    params["limit"] = limit

    params["offset"] = offset

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/issues",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | IssuesGetResponse | None:
    if response.status_code == 200:
        response_200 = IssuesGetResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | IssuesGetResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    source: IssueSource | None | Unset = UNSET,
    project: None | str | Unset = UNSET,
    status: IssueStatus | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    q: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | IssuesGetResponse]:
    """Get Issues

    Args:
        source (IssueSource | None | Unset): Filter by issue source (e.g., github, jira,
            launchpad)
        project (None | str | Unset): Filter by project name
        status (IssueStatus | None | Unset): Filter by issue status (e.g., open, closed, unknown)
        limit (int | Unset): Maximum number of results to return (default: 50) Default: 50.
        offset (int | Unset): Number of results to skip for pagination (default: 0) Default: 0.
        q (None | str | Unset): Search term for issue source, project, keys, title, and status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | IssuesGetResponse]
    """

    kwargs = _get_kwargs(
        source=source,
        project=project,
        status=status,
        limit=limit,
        offset=offset,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    source: IssueSource | None | Unset = UNSET,
    project: None | str | Unset = UNSET,
    status: IssueStatus | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    q: None | str | Unset = UNSET,
) -> HTTPValidationError | IssuesGetResponse | None:
    """Get Issues

    Args:
        source (IssueSource | None | Unset): Filter by issue source (e.g., github, jira,
            launchpad)
        project (None | str | Unset): Filter by project name
        status (IssueStatus | None | Unset): Filter by issue status (e.g., open, closed, unknown)
        limit (int | Unset): Maximum number of results to return (default: 50) Default: 50.
        offset (int | Unset): Number of results to skip for pagination (default: 0) Default: 0.
        q (None | str | Unset): Search term for issue source, project, keys, title, and status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | IssuesGetResponse
    """

    return sync_detailed(
        client=client,
        source=source,
        project=project,
        status=status,
        limit=limit,
        offset=offset,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    source: IssueSource | None | Unset = UNSET,
    project: None | str | Unset = UNSET,
    status: IssueStatus | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    q: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | IssuesGetResponse]:
    """Get Issues

    Args:
        source (IssueSource | None | Unset): Filter by issue source (e.g., github, jira,
            launchpad)
        project (None | str | Unset): Filter by project name
        status (IssueStatus | None | Unset): Filter by issue status (e.g., open, closed, unknown)
        limit (int | Unset): Maximum number of results to return (default: 50) Default: 50.
        offset (int | Unset): Number of results to skip for pagination (default: 0) Default: 0.
        q (None | str | Unset): Search term for issue source, project, keys, title, and status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | IssuesGetResponse]
    """

    kwargs = _get_kwargs(
        source=source,
        project=project,
        status=status,
        limit=limit,
        offset=offset,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    source: IssueSource | None | Unset = UNSET,
    project: None | str | Unset = UNSET,
    status: IssueStatus | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    q: None | str | Unset = UNSET,
) -> HTTPValidationError | IssuesGetResponse | None:
    """Get Issues

    Args:
        source (IssueSource | None | Unset): Filter by issue source (e.g., github, jira,
            launchpad)
        project (None | str | Unset): Filter by project name
        status (IssueStatus | None | Unset): Filter by issue status (e.g., open, closed, unknown)
        limit (int | Unset): Maximum number of results to return (default: 50) Default: 50.
        offset (int | Unset): Number of results to skip for pagination (default: 0) Default: 0.
        q (None | str | Unset): Search term for issue source, project, keys, title, and status

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | IssuesGetResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            source=source,
            project=project,
            status=status,
            limit=limit,
            offset=offset,
            q=q,
        )
    ).parsed
