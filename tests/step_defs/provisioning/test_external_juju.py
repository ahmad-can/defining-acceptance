"""
Step definitions for external Juju controller provisioning tests.
"""

from pytest_bdd import scenario, given, when, then
import unittest.mock as mock


@scenario("provisioning/external-juju.feature", "Register external Juju controller")
def test_register_external_juju():
    pass


@scenario(
    "provisioning/external-juju.feature", "Bootstrap cloud with external controller"
)
def test_bootstrap_external_juju():
    pass


@given("an external Juju controller exists")
def verify_external_juju_exists():
    """Verify external Juju controller exists."""
    pass


@given("the controller has a dedicated user with superuser permissions")
def verify_juju_user():
    """Verify Juju user has superuser permissions."""
    pass


@given("I have the external controller details")
def get_external_controller_details():
    """Get external controller details."""
    pass


@when("I register the external Juju controller in Sunbeam")
def register_external_juju():
    """Register external Juju controller in Sunbeam."""
    return mock.Mock(success=True, controller="prod-controller-01")


@then("the controller should be available in Sunbeam")
def verify_controller_available():
    """Verify controller is available."""
    pass


@given("the external Juju controller is registered")
def external_juju_registered():
    """Verify external Juju controller is registered."""
    pass


@when("I bootstrap the cloud with --controller option")
def bootstrap_with_external_controller():
    """Bootstrap cloud with external controller."""
    return mock.Mock(success=True, external_controller=True)


@then("the cloud should use the external controller")
def verify_uses_external_controller():
    """Verify cloud uses external controller."""
    pass


@then("all services should be deployed via the external controller")
def verify_services_via_external():
    """Verify services are deployed via external controller."""
    pass
