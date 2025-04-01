from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_homepage():
    response = client.get("/")
    print(response.text)  # Debugging line
    assert response.status_code == 200
    assert "<title>My Profile</title>" in response.text