import pytest

from utils.api_client import APIClient


@pytest.fixture
def api_client():

    client = APIClient()

    yield client

    client.close()