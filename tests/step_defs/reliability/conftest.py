"""
Shared step definitions for reliability tests.
Common steps used across multiple reliability scenarios.
"""

import pytest
from pytest_bdd import given


# Common steps shared across reliability tests
@given("all VMs are reachable via SSH")
def verify_ssh_connectivity():
    # Logic to verify SSH connectivity to all VMs
    pass


@given("a running VM")
def setup_running_vm():
    # Logic to ensure a VM is running
    pass


@given("multiple VMs on the same network")
def setup_multiple_vms():
    # Logic to setup multiple VMs on the same network
    pass
