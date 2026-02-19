from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.family_name import FamilyName
from ...models.http_validation_error import HTTPValidationError
from ...models.pending_rerun import PendingRerun
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    family: FamilyName | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    environment: None | str | Unset = UNSET,
    environment_architecture: None | str | Unset = UNSET,
    build_architecture: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_family: None | str | Unset
    if isinstance(family, Unset):
        json_family = UNSET
    elif isinstance(family, FamilyName):
        json_family = family.value
    else:
        json_family = family
    params["family"] = json_family

    json_limit: int | None | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_environment: None | str | Unset
    if isinstance(environment, Unset):
        json_environment = UNSET
    else:
        json_environment = environment
    params["environment"] = json_environment

    json_environment_architecture: None | str | Unset
    if isinstance(environment_architecture, Unset):
        json_environment_architecture = UNSET
    else:
        json_environment_architecture = environment_architecture
    params["environment_architecture"] = json_environment_architecture

    json_build_architecture: None | str | Unset
    if isinstance(build_architecture, Unset):
        json_build_architecture = UNSET
    else:
        json_build_architecture = build_architecture
    params["build_architecture"] = json_build_architecture

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/test-executions/reruns",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[PendingRerun] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PendingRerun.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[PendingRerun]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    family: FamilyName | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    environment: None | str | Unset = UNSET,
    environment_architecture: None | str | Unset = UNSET,
    build_architecture: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[PendingRerun]]:
    """Get Rerun Requests

    Args:
        family (FamilyName | None | Unset):
        limit (int | None | Unset):
        environment (None | str | Unset):
        environment_architecture (None | str | Unset):
        build_architecture (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[PendingRerun]]
    """

    kwargs = _get_kwargs(
        family=family,
        limit=limit,
        environment=environment,
        environment_architecture=environment_architecture,
        build_architecture=build_architecture,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    family: FamilyName | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    environment: None | str | Unset = UNSET,
    environment_architecture: None | str | Unset = UNSET,
    build_architecture: None | str | Unset = UNSET,
) -> HTTPValidationError | list[PendingRerun] | None:
    """Get Rerun Requests

    Args:
        family (FamilyName | None | Unset):
        limit (int | None | Unset):
        environment (None | str | Unset):
        environment_architecture (None | str | Unset):
        build_architecture (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[PendingRerun]
    """

    return sync_detailed(
        client=client,
        family=family,
        limit=limit,
        environment=environment,
        environment_architecture=environment_architecture,
        build_architecture=build_architecture,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    family: FamilyName | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    environment: None | str | Unset = UNSET,
    environment_architecture: None | str | Unset = UNSET,
    build_architecture: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[PendingRerun]]:
    """Get Rerun Requests

    Args:
        family (FamilyName | None | Unset):
        limit (int | None | Unset):
        environment (None | str | Unset):
        environment_architecture (None | str | Unset):
        build_architecture (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[PendingRerun]]
    """

    kwargs = _get_kwargs(
        family=family,
        limit=limit,
        environment=environment,
        environment_architecture=environment_architecture,
        build_architecture=build_architecture,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    family: FamilyName | None | Unset = UNSET,
    limit: int | None | Unset = UNSET,
    environment: None | str | Unset = UNSET,
    environment_architecture: None | str | Unset = UNSET,
    build_architecture: None | str | Unset = UNSET,
) -> HTTPValidationError | list[PendingRerun] | None:
    """Get Rerun Requests

    Args:
        family (FamilyName | None | Unset):
        limit (int | None | Unset):
        environment (None | str | Unset):
        environment_architecture (None | str | Unset):
        build_architecture (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[PendingRerun]
    """

    return (
        await asyncio_detailed(
            client=client,
            family=family,
            limit=limit,
            environment=environment,
            environment_architecture=environment_architecture,
            build_architecture=build_architecture,
        )
    ).parsed
