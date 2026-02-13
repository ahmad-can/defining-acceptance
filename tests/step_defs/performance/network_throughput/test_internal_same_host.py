import pytest
from pytest_bdd import scenario, given, when
import unittest.mock as mock


@scenario(
    "performance/network_throughput.feature", "Internal network throughput on same host"
)
def test_internal_network_same_host():
    # Pytest-bdd requires this stub to tie the scenario together
    pass


# Scenario-specific step
@given("two VMs on the same network and host")
def setup_vms_same_host():
    # Logic to setup two VMs on the same network and host
    pass


@pytest.fixture
@when("I measure throughput between them")
def measure_throughput():
    # Logic to measure throughput between VMs on same host
    # Example: using iperf3 or similar tool
    return mock.Mock(throughput_gbps=1.5)
