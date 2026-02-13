"""
Shared step definitions for network throughput tests.
Common steps used across multiple network performance scenarios.
"""

import pytest
from pytest_bdd import given, then
import unittest.mock as mock


# Background step specific to network throughput tests
@given("all VMs are reachable via SSH")
def verify_ssh_connectivity():
    # Logic to verify SSH connectivity
    pass


# Common assertion for throughput tests
@then("throughput should be at least 1 Gbps")
def check_throughput_1gbps(measure_throughput):
    # Assert throughput is at least 1 Gbps
    assert measure_throughput.throughput_gbps >= 1.0, (
        f"Throughput {measure_throughput.throughput_gbps} Gbps is below 1 Gbps"
    )
