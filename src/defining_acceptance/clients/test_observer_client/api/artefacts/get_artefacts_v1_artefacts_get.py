from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.artefact_response import ArtefactResponse
from ...models.family_name import FamilyName
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    family: FamilyName | None | Unset = UNSET,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/artefacts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[ArtefactResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ArtefactResponse.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[ArtefactResponse]]:
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
) -> Response[HTTPValidationError | list[ArtefactResponse]]:
    """Get Artefacts

     Get latest artefacts optionally by family

    Args:
        family (FamilyName | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ArtefactResponse]]
    """

    kwargs = _get_kwargs(
        family=family,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    family: FamilyName | None | Unset = UNSET,
) -> HTTPValidationError | list[ArtefactResponse] | None:
    """Get Artefacts

     Get latest artefacts optionally by family

    Args:
        family (FamilyName | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ArtefactResponse]
    """

    return sync_detailed(
        client=client,
        family=family,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    family: FamilyName | None | Unset = UNSET,
) -> Response[HTTPValidationError | list[ArtefactResponse]]:
    """Get Artefacts

     Get latest artefacts optionally by family

    Args:
        family (FamilyName | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ArtefactResponse]]
    """

    kwargs = _get_kwargs(
        family=family,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    family: FamilyName | None | Unset = UNSET,
) -> HTTPValidationError | list[ArtefactResponse] | None:
    """Get Artefacts

     Get latest artefacts optionally by family

    Args:
        family (FamilyName | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ArtefactResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            family=family,
        )
    ).parsed
