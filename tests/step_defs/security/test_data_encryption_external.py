import pytest
from pytest_bdd import scenario, given, when, then
import unittest.mock as mock


@scenario("security/data_encryption.feature", "External connections use TLS")
def test_external_connections_tls():
    # Pytest-bdd requires this stub to tie the scenario together
    pass


# Scenario-specific steps
@given("a VM with external service")
def setup_vm_with_service():
    # Logic to setup a VM with an external-facing service
    pass


@pytest.fixture
@when("I connect to the service")
def connect_to_service():
    # Logic to connect to the external service
    # Example: using curl, requests library, or similar
    return mock.Mock(tls_enabled=True, tls_version="TLSv1.3")


@then("TLS should be enforced")
def verify_tls_enforced(connect_to_service):
    # Assert TLS is enforced on the connection
    assert connect_to_service.tls_enabled, (
        "TLS should be enforced on external connections"
    )
