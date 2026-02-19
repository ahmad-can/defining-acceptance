from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.family_name import FamilyName
from ...models.http_validation_error import HTTPValidationError
from ...models.test_cases_response import TestCasesResponse
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
        "url": "/v1/test-cases",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | TestCasesResponse | None:
    if response.status_code == 200:
        response_200 = TestCasesResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | TestCasesResponse]:
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
) -> Response[HTTPValidationError | TestCasesResponse]:
    r"""Get Test Cases

     Returns test cases as a flat list with their template IDs.

    Template ID represents the generic test (e.g., \"disk/stats_name\")
    Test case name is the specific instance (e.g., \"disk/stats_nvme0n1\")
    Multiple test cases can share the same template ID but have different names.

    Args:
        q (None | str | Unset): Search term for test case names
        families (list[FamilyName] | None | Unset): Filter by artefact families
        limit (int | Unset): Maximum number of results (defaults to 50 if not specified) Default:
            50.
        offset (int | Unset): Number of results to skip for pagination Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TestCasesResponse]
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
) -> HTTPValidationError | TestCasesResponse | None:
    r"""Get Test Cases

     Returns test cases as a flat list with their template IDs.

    Template ID represents the generic test (e.g., \"disk/stats_name\")
    Test case name is the specific instance (e.g., \"disk/stats_nvme0n1\")
    Multiple test cases can share the same template ID but have different names.

    Args:
        q (None | str | Unset): Search term for test case names
        families (list[FamilyName] | None | Unset): Filter by artefact families
        limit (int | Unset): Maximum number of results (defaults to 50 if not specified) Default:
            50.
        offset (int | Unset): Number of results to skip for pagination Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TestCasesResponse
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
) -> Response[HTTPValidationError | TestCasesResponse]:
    r"""Get Test Cases

     Returns test cases as a flat list with their template IDs.

    Template ID represents the generic test (e.g., \"disk/stats_name\")
    Test case name is the specific instance (e.g., \"disk/stats_nvme0n1\")
    Multiple test cases can share the same template ID but have different names.

    Args:
        q (None | str | Unset): Search term for test case names
        families (list[FamilyName] | None | Unset): Filter by artefact families
        limit (int | Unset): Maximum number of results (defaults to 50 if not specified) Default:
            50.
        offset (int | Unset): Number of results to skip for pagination Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | TestCasesResponse]
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
) -> HTTPValidationError | TestCasesResponse | None:
    r"""Get Test Cases

     Returns test cases as a flat list with their template IDs.

    Template ID represents the generic test (e.g., \"disk/stats_name\")
    Test case name is the specific instance (e.g., \"disk/stats_nvme0n1\")
    Multiple test cases can share the same template ID but have different names.

    Args:
        q (None | str | Unset): Search term for test case names
        families (list[FamilyName] | None | Unset): Filter by artefact families
        limit (int | Unset): Maximum number of results (defaults to 50 if not specified) Default:
            50.
        offset (int | Unset): Number of results to skip for pagination Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | TestCasesResponse
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
