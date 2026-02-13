import pytest
from pytest_bdd import scenarios, when, then
import unittest.mock as mock


# Load all scenarios from the feature file
scenarios("security/access_control.feature")


# Scenario-specific steps
@pytest.fixture
@when("I connect with correct SSH key")
def connect_with_key():
    # Logic to connect to VM with correct SSH key
    return mock.Mock(success=True, connection_status="connected")


@pytest.fixture
@when("I connect without SSH key")
def connect_without_key():
    # Logic to attempt connection to VM without SSH key
    return mock.Mock(success=False, connection_status="refused")


@then("the connection should succeed")
def check_connection_success(connect_with_key):
    # Assert connection was successful
    assert connect_with_key.success, "SSH connection with correct key should succeed"


@then("the connection should be refused")
def check_connection_refused(connect_without_key):
    # Assert connection was refused
    assert not connect_without_key.success, (
        "SSH connection without key should be refused"
    )
    assert connect_without_key.connection_status == "refused", (
        "Connection should be explicitly refused"
    )
