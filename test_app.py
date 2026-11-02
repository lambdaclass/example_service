import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_version(client):
    response = client.get("/version")
    assert response.status_code == 200
    assert response.get_json() == {"version": "0.1.0"}
