from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_sum():
    response = client.get("/sum?a=5&b=3")
    assert response.status_code == 200
    assert response.json()["result"] == 8