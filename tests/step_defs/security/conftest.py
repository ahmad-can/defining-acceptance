"""
Shared step definitions for security tests.
Common steps used across multiple security scenarios.
"""

import pytest
from pytest_bdd import given


# Common step for VM setup - shared across security tests
@given("a VM")
def setup_vm():
    # Logic to setup/provision a VM
    pass
