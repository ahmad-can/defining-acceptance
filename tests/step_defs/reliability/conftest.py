"""
Shared step definitions for reliability tests.
"""

from pytest_bdd import given


@given("the cloud is provisioned")
def cloud_provisioned():
    pass


@given("the cloud is configured for sample usage")
def cloud_configured():
    pass


@given("a VM is running")
def setup_running_vm():
    pass


@given("multiple VMs are running on the same network")
def setup_multiple_vms():
    pass
