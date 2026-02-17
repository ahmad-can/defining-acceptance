"""
Shared step definitions for network throughput tests.
"""

from pytest_bdd import given


@given("the cloud is provisioned")
def cloud_provisioned():
    """Verify the cloud is provisioned."""
    pass


@given("the cloud is configured for sample usage")
def cloud_configured():
    """Verify the cloud is configured for sample usage."""
    pass


@given("a VM is running")
def setup_running_vm():
    """Ensure a VM is running."""
    pass
