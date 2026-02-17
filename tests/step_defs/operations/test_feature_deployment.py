
from pytest_bdd import scenarios


# Load all scenario outlines from the feature file
# Step definitions are in conftest.py
scenarios("operations/deployments.feature")
