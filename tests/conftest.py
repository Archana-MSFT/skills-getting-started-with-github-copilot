import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(autouse=True)
def reset_activities_store():
    """Restore in-memory activities after each test for isolation."""
    # Arrange
    original_activities = copy.deepcopy(app_module.activities)

    # Act
    yield

    # Assert
    app_module.activities.clear()
    app_module.activities.update(original_activities)


@pytest.fixture
def client():
    """Provide a FastAPI test client."""
    return TestClient(app_module.app)
