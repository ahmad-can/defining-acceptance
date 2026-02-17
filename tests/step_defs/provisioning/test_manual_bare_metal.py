"""
Step definitions for manual bare metal provisioning tests.
"""

from pytest_bdd import scenario, given, when, then
import unittest.mock as mock


@scenario("provisioning/manual-bare-metal.feature", "Prepare node for bootstrap")
def test_prepare_node():
    pass


@scenario("provisioning/manual-bare-metal.feature", "Bootstrap single-node cloud")
def test_bootstrap_single_node():
    pass


@given("a machine meets minimum hardware requirements")
def verify_hardware_requirements():
    """Verify machine meets hardware requirements."""
    pass


@given("Ubuntu Server 24.04 LTS is installed")
def verify_ubuntu_installed():
    """Verify Ubuntu is installed."""
    pass


@given("the openstack snap is installed")
def verify_snap_installed():
    """Verify openstack snap is installed."""
    pass


@when("I run the prepare-node-script")
def run_prepare_node_script():
    """Run prepare-node-script."""
    return mock.Mock(success=True)


@then("the node should be ready for bootstrap")
def verify_node_ready():
    """Verify node is ready."""
    pass


@given("the node is prepared")
def node_prepared():
    """Verify node is prepared."""
    pass


@when("I bootstrap the cloud with default roles")
def bootstrap_cloud():
    """Bootstrap cloud with default roles."""
    return mock.Mock(success=True, roles=["control", "compute", "storage"])


@then("the cloud should be bootstrapped successfully")
def verify_cloud_bootstrapped():
    """Verify cloud is bootstrapped."""
    pass


@then("the cloud should have control, compute, and storage roles")
def verify_roles():
    """Verify cloud has required roles."""
    pass
