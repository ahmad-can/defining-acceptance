from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.environments_response import EnvironmentsResponse
from ...models.family_name import FamilyName
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: None | str | Unset = UNSET,
    families: list[FamilyName] | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_q: None | str | Unset
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

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

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/environments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EnvironmentsResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EnvironmentsResponse.from_dict(response.json())

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
) -> Response[EnvironmentsResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: None | str | Unset = UNSET,
    families: list[FamilyName] | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> Response[EnvironmentsResponse | HTTPValidationError]:
    """Get Environments

     Returns list of distinct environments that have been used in test executions.

    Supports pagination and search filtering.

    Args:
        q (None | str | Unset): Search term for environment names
        families (list[FamilyName] | None | Unset): Filter by artefact families
        limit (int | Unset): Maximum number of results (defaults to 50 if not specified) Default:
            50.
        offset (int | Unset): Number of results to skip for pagination Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnvironmentsResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        q=q,
        families=families,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    q: None | str | Unset = UNSET,
    families: list[FamilyName] | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> EnvironmentsResponse | HTTPValidationError | None:
    """Get Environments

     Returns list of distinct environments that have been used in test executions.

    Supports pagination and search filtering.

    Args:
        q (None | str | Unset): Search term for environment names
        families (list[FamilyName] | None | Unset): Filter by artefact families
        limit (int | Unset): Maximum number of results (defaults to 50 if not specified) Default:
            50.
        offset (int | Unset): Number of results to skip for pagination Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnvironmentsResponse | HTTPValidationError
    """

    return sync_detailed(
        client=client,
        q=q,
        families=families,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: None | str | Unset = UNSET,
    families: list[FamilyName] | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> Response[EnvironmentsResponse | HTTPValidationError]:
    """Get Environments

     Returns list of distinct environments that have been used in test executions.

    Supports pagination and search filtering.

    Args:
        q (None | str | Unset): Search term for environment names
        families (list[FamilyName] | None | Unset): Filter by artefact families
        limit (int | Unset): Maximum number of results (defaults to 50 if not specified) Default:
            50.
        offset (int | Unset): Number of results to skip for pagination Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EnvironmentsResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        q=q,
        families=families,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: None | str | Unset = UNSET,
    families: list[FamilyName] | None | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> EnvironmentsResponse | HTTPValidationError | None:
    """Get Environments

     Returns list of distinct environments that have been used in test executions.

    Supports pagination and search filtering.

    Args:
        q (None | str | Unset): Search term for environment names
        families (list[FamilyName] | None | Unset): Filter by artefact families
        limit (int | Unset): Maximum number of results (defaults to 50 if not specified) Default:
            50.
        offset (int | Unset): Number of results to skip for pagination Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EnvironmentsResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            families=families,
            limit=limit,
            offset=offset,
        )
    ).parsed
