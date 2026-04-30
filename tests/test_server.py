import pytest
from src.server import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_returns_200_html(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Hello from CI/CD" in res.data
    assert b"text/html" in res.content_type.encode()


def test_health_returns_ok(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}
