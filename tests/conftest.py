import pytest
from starlette.config import environ
from starlette.testclient import TestClient

environ["API_KEY"] = "1234"

from ppipe.webservice.main import get_app

@pytest.fixture()
def test_client():
    app = get_app()
    with TestClient(app) as test_client:
        yield test_client
