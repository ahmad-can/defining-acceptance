import pytest
from pytest_bdd import scenario, given, when, then
import unittest.mock as mock


@scenario("performance/network_throughput.feature", "External network throughput")
def test_external_network_throughput():
    # Pytest-bdd requires this stub to tie the scenario together
    pass


# Scenario-specific steps
@given("a running VM")
def setup_running_vm():
    # Logic to ensure a VM is running
    pass


@pytest.fixture
@when("I download data from external source")
def download_from_external():
    # Logic to download data from external source
    # Example: using wget, curl, or similar tool
    return mock.Mock(download_speed_mbps=100)


@then("download speed should be acceptable")
def check_download_speed(download_from_external):
    # Assert download speed is acceptable (define threshold as needed)
    min_acceptable_speed = 10  # Mbps
    assert download_from_external.download_speed_mbps >= min_acceptable_speed, (
        f"Download speed {download_from_external.download_speed_mbps} Mbps is below acceptable threshold of {min_acceptable_speed} Mbps"
    )
