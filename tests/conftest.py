import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture
def client():
    initial_activities = copy.deepcopy(app_module.activities)

    try:
        with TestClient(app_module.app) as client:
            yield client
    finally:
        app_module.activities.clear()
        app_module.activities.update(initial_activities)
