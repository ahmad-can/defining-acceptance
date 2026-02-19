"""Shared step definitions for network throughput performance tests."""

import os

import pytest
from pytest_bdd import given

from defining_acceptance.reporting import report
from tests._vm_helpers import create_vm, vm_ssh

MOCK_MODE = os.environ.get("MOCK_MODE", "0") == "1"

# "the cloud is provisioned" is defined in tests/conftest.py and applies here.


@given("the cloud is configured for sample usage")
def cloud_configured(demo_os_runner):
    """Verify the cloud has the basic resources needed to run workloads."""
    if MOCK_MODE:
        return
    with report.step("Verifying cloud is configured for sample usage"):
        flavors = demo_os_runner.flavor_list()
        assert flavors, "No flavors found — run 'sunbeam configure' first"

        images = demo_os_runner.image_list()
        assert images, "No images found — run 'sunbeam configure' first"

        networks = demo_os_runner.network_list()
        assert networks, "No networks found — run 'sunbeam configure' first"

        report.note(
            f"Found {len(flavors)} flavor(s), "
            f"{len(images)} image(s), "
            f"{len(networks)} network(s)"
        )


@pytest.fixture
def running_vm() -> dict:
    """Mutable container populated by 'a VM is running' (the iperf server)."""
    return {}


@given("a VM is running")
def setup_running_vm(demo_os_runner, testbed, ssh_runner, running_vm, request):
    """Create the iperf server VM with a floating IP."""
    if MOCK_MODE:
        running_vm.update(
            {
                "server_id": "mock-server",
                "server_name": "mock-vm",
                "key_path": "/tmp/mock.pem",
                "primary_ip": "192.168.1.100",
                "floating_ip": "192.0.2.1",
                "internal_ip": "10.0.0.5",
                "network_name": "default",
            }
        )
        return
    resources = create_vm(demo_os_runner, testbed, ssh_runner, request)
    running_vm.update(resources)

    # Install iperf3 on the server VM.
    with report.step("Installing iperf3 on server VM"):
        vm_ssh(
            ssh_runner,
            resources["primary_ip"],
            resources["floating_ip"],
            resources["key_path"],
            "sudo apt-get install -y iperf3 -qq 2>/dev/null || true",
            timeout=120,
        )

    # Start iperf3 in server mode (background, exits on first client).
    vm_ssh(
        ssh_runner,
        resources["primary_ip"],
        resources["floating_ip"],
        resources["key_path"],
        "iperf3 -s -D -1",  # -D daemonize, -1 exit after one client
        timeout=15,
    )
    report.note(
        f"iperf3 server running on VM at {resources['floating_ip']} "
        f"(internal: {resources['internal_ip']})"
    )
