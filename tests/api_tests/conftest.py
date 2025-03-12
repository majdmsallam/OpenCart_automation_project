import pytest
from tests.api_tests.api_client import APIClient

BASE_URL = "https://www.automationexercise.com/api"

@pytest.fixture(scope="module")
def api_client():
    return APIClient(BASE_URL)