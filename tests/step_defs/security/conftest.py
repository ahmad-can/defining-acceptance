"""Shared step definitions for security tests."""

import os

import pytest
from pytest_bdd import given

from defining_acceptance.reporting import report
from tests._vm_helpers import create_vm

MOCK_MODE = os.environ.get("MOCK_MODE", "0") == "1"

# "the cloud is provisioned" is defined in tests/conftest.py and applies here.


@given("the cloud is configured for sample usage")
def cloud_configured(openstack_client):
    """Verify the cloud has the basic resources needed to run workloads."""
    if MOCK_MODE:
        return
    with report.step("Verifying cloud is configured for sample usage"):
        flavors = openstack_client.flavor_list()
        assert flavors, "No flavors found — run 'sunbeam configure' first"

        images = openstack_client.image_list()
        assert images, "No images found — run 'sunbeam configure' first"

        networks = openstack_client.network_list()
        assert networks, "No networks found — run 'sunbeam configure' first"

        report.note(
            f"Found {len(flavors)} flavor(s), "
            f"{len(images)} image(s), "
            f"{len(networks)} network(s)"
        )


@pytest.fixture
def running_vm() -> dict:
    """Mutable container populated by 'a VM is running'."""
    return {}


@pytest.fixture
def second_vm() -> dict:
    """Mutable container populated by steps that create an additional VM."""
    return {}


@given("a VM is running")
def setup_running_vm(openstack_client, testbed, ssh_runner, running_vm, request):
    """Create a VM with a floating IP and wait for SSH to become available."""
    if MOCK_MODE:
        running_vm.update(
            {
                "server_id": "mock-server",
                "server_name": "mock-vm",
                "keypair_name": "mock-key",
                "key_path": "/tmp/mock.pem",
                "primary_ip": "192.168.1.100",
                "floating_ip": "192.0.2.1",
                "internal_ip": "10.0.0.5",
                "network_name": "default",
            }
        )
        return
    resources = create_vm(openstack_client, testbed, ssh_runner, request)
    running_vm.update(resources)
    report.note(f"VM {resources['server_name']} running at {resources['floating_ip']}")
