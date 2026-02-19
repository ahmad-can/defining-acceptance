from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.artefact_build_environment_review_response import (
    ArtefactBuildEnvironmentReviewResponse,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    artefact_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/artefacts/{artefact_id}/environment-reviews".format(
            artefact_id=quote(str(artefact_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[ArtefactBuildEnvironmentReviewResponse] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ArtefactBuildEnvironmentReviewResponse.from_dict(
                response_200_item_data
            )

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
) -> Response[HTTPValidationError | list[ArtefactBuildEnvironmentReviewResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    artefact_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | list[ArtefactBuildEnvironmentReviewResponse]]:
    """Get Environment Reviews

    Args:
        artefact_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ArtefactBuildEnvironmentReviewResponse]]
    """

    kwargs = _get_kwargs(
        artefact_id=artefact_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    artefact_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | list[ArtefactBuildEnvironmentReviewResponse] | None:
    """Get Environment Reviews

    Args:
        artefact_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ArtefactBuildEnvironmentReviewResponse]
    """

    return sync_detailed(
        artefact_id=artefact_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    artefact_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | list[ArtefactBuildEnvironmentReviewResponse]]:
    """Get Environment Reviews

    Args:
        artefact_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[ArtefactBuildEnvironmentReviewResponse]]
    """

    kwargs = _get_kwargs(
        artefact_id=artefact_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    artefact_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | list[ArtefactBuildEnvironmentReviewResponse] | None:
    """Get Environment Reviews

    Args:
        artefact_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[ArtefactBuildEnvironmentReviewResponse]
    """

    return (
        await asyncio_detailed(
            artefact_id=artefact_id,
            client=client,
        )
    ).parsed
