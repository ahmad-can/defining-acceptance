from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.issue_test_result_attachment_rule_patch_request import (
    IssueTestResultAttachmentRulePatchRequest,
)
from ...models.minimal_issue_test_result_attachment_rule_response import (
    MinimalIssueTestResultAttachmentRuleResponse,
)
from ...types import Response


def _get_kwargs(
    issue_id: int,
    attachment_rule_id: int,
    *,
    body: IssueTestResultAttachmentRulePatchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/issues/{issue_id}/attachment-rules/{attachment_rule_id}".format(
            issue_id=quote(str(issue_id), safe=""),
            attachment_rule_id=quote(str(attachment_rule_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | MinimalIssueTestResultAttachmentRuleResponse | None:
    if response.status_code == 200:
        response_200 = MinimalIssueTestResultAttachmentRuleResponse.from_dict(
            response.json()
        )

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
) -> Response[HTTPValidationError | MinimalIssueTestResultAttachmentRuleResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    issue_id: int,
    attachment_rule_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: IssueTestResultAttachmentRulePatchRequest,
) -> Response[HTTPValidationError | MinimalIssueTestResultAttachmentRuleResponse]:
    """Patch Attachment Rule

    Args:
        issue_id (int):
        attachment_rule_id (int):
        body (IssueTestResultAttachmentRulePatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MinimalIssueTestResultAttachmentRuleResponse]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        attachment_rule_id=attachment_rule_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    issue_id: int,
    attachment_rule_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: IssueTestResultAttachmentRulePatchRequest,
) -> HTTPValidationError | MinimalIssueTestResultAttachmentRuleResponse | None:
    """Patch Attachment Rule

    Args:
        issue_id (int):
        attachment_rule_id (int):
        body (IssueTestResultAttachmentRulePatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MinimalIssueTestResultAttachmentRuleResponse
    """

    return sync_detailed(
        issue_id=issue_id,
        attachment_rule_id=attachment_rule_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    issue_id: int,
    attachment_rule_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: IssueTestResultAttachmentRulePatchRequest,
) -> Response[HTTPValidationError | MinimalIssueTestResultAttachmentRuleResponse]:
    """Patch Attachment Rule

    Args:
        issue_id (int):
        attachment_rule_id (int):
        body (IssueTestResultAttachmentRulePatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MinimalIssueTestResultAttachmentRuleResponse]
    """

    kwargs = _get_kwargs(
        issue_id=issue_id,
        attachment_rule_id=attachment_rule_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    issue_id: int,
    attachment_rule_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: IssueTestResultAttachmentRulePatchRequest,
) -> HTTPValidationError | MinimalIssueTestResultAttachmentRuleResponse | None:
    """Patch Attachment Rule

    Args:
        issue_id (int):
        attachment_rule_id (int):
        body (IssueTestResultAttachmentRulePatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MinimalIssueTestResultAttachmentRuleResponse
    """

    return (
        await asyncio_detailed(
            issue_id=issue_id,
            attachment_rule_id=attachment_rule_id,
            client=client,
            body=body,
        )
    ).parsed
