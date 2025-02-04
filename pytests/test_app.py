import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Darvin Xavier" in response.data  # Check if response contains expected text

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "OK"}
