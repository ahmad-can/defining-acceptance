from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.pending_rerun import PendingRerun
from ...models.rerun_request import RerunRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RerunRequest,
    silent: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["silent"] = silent

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/test-executions/reruns",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[PendingRerun] | None | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> list[PendingRerun] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_0 = []
                _response_200_type_0 = data
                for response_200_type_0_item_data in _response_200_type_0:
                    response_200_type_0_item = PendingRerun.from_dict(
                        response_200_type_0_item_data
                    )

                    response_200_type_0.append(response_200_type_0_item)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PendingRerun] | None, data)

        response_200 = _parse_response_200(response.json())

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
) -> Response[HTTPValidationError | list[PendingRerun] | None]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RerunRequest,
    silent: bool | Unset = False,
) -> Response[HTTPValidationError | list[PendingRerun] | None]:
    """Create Rerun Requests

    Args:
        silent (bool | Unset): If true, omit returning created reruns in the response body. Speeds
            up bulk operations, as the rerun schema contains a lot of information and returning many
            reruns can be slow. Required when creating reruns with test result filters. Default:
            False.
        body (RerunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[PendingRerun] | None]
    """

    kwargs = _get_kwargs(
        body=body,
        silent=silent,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RerunRequest,
    silent: bool | Unset = False,
) -> HTTPValidationError | list[PendingRerun] | None | None:
    """Create Rerun Requests

    Args:
        silent (bool | Unset): If true, omit returning created reruns in the response body. Speeds
            up bulk operations, as the rerun schema contains a lot of information and returning many
            reruns can be slow. Required when creating reruns with test result filters. Default:
            False.
        body (RerunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[PendingRerun] | None
    """

    return sync_detailed(
        client=client,
        body=body,
        silent=silent,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RerunRequest,
    silent: bool | Unset = False,
) -> Response[HTTPValidationError | list[PendingRerun] | None]:
    """Create Rerun Requests

    Args:
        silent (bool | Unset): If true, omit returning created reruns in the response body. Speeds
            up bulk operations, as the rerun schema contains a lot of information and returning many
            reruns can be slow. Required when creating reruns with test result filters. Default:
            False.
        body (RerunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[PendingRerun] | None]
    """

    kwargs = _get_kwargs(
        body=body,
        silent=silent,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RerunRequest,
    silent: bool | Unset = False,
) -> HTTPValidationError | list[PendingRerun] | None | None:
    """Create Rerun Requests

    Args:
        silent (bool | Unset): If true, omit returning created reruns in the response body. Speeds
            up bulk operations, as the rerun schema contains a lot of information and returning many
            reruns can be slow. Required when creating reruns with test result filters. Default:
            False.
        body (RerunRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[PendingRerun] | None
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            silent=silent,
        )
    ).parsed
