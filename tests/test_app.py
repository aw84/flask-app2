import pytest
from app import create_app


@pytest.fixture
def app():
    app = create_app('TEST')
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_config():
    assert create_app('TEST').testing
    assert create_app('DEV').debug


def test_hello(client):
    response = client.get("/")
    assert response.status_code == 404
