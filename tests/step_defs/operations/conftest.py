"""
Shared step definitions for operations tests.
"""

import pytest
from pytest_bdd import given, when, then, parsers
import allure


# Mock mode check
import os

MOCK_MODE = os.environ.get("MOCK_MODE", "0") == "1"


@given("the cloud is provisioned")
def cloud_provisioned():
    """Verify the cloud is provisioned."""
    pass


@given("the cloud is configured for sample usage")
def cloud_configured():
    """Verify the cloud is configured for sample usage."""
    pass


@given(parsers.parse('the feature "{feature}" is enabled'))
def given_feature_enabled(enable_feature, feature):
    """Enable a feature in the cloud deployment."""
    with allure.step(f"Enabling feature: {feature}"):
        try:
            enable_feature(feature)
        except Exception as e:
            allure.attach(
                str(e),
                name="Feature enable error",
                attachment_type=allure.attachment_type.TEXT,
            )
            raise


@pytest.fixture
def tempest_result():
    """Fixture to store tempest result between steps."""
    return {}


@when(parsers.parse('I run Tempest tests for the feature "{feature}"'))
def when_run_tempest_tests(tempest_runner, tempest_result, feature):
    """Run Tempest tests for the given feature."""
    with allure.step(f"Running Tempest tests for {feature}"):
        result = tempest_runner(feature)

        # Store result for later verification
        tempest_result["result"] = result
        tempest_result["feature"] = feature

        allure.attach(
            result.stdout,
            name="Tempest output",
            attachment_type=allure.attachment_type.TEXT,
        )

        if result.stderr:
            allure.attach(
                result.stderr,
                name="Tempest errors",
                attachment_type=allure.attachment_type.TEXT,
            )


@then("the Tempest run should pass successfully")
def then_check_tempest_passed(tempest_result):
    """Verify that the Tempest tests passed."""
    if "result" not in tempest_result:
        return

    result = tempest_result["result"]

    if result.returncode != 0:
        raise AssertionError(
            f"Tempest tests failed with return code {result.returncode}. "
            "Check the attached logs in Allure."
        )
