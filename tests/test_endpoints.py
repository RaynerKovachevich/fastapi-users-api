import pytest
from fastapi.testclient import TestClient
from main import app
from database import get_db
import models
import uuid

client = TestClient(app)

@pytest.fixture
def clean_user_table():
    db = next(get_db())
    try:
        db.query(models.User).delete()
        db.commit()
        yield
    finally:
        db.query(models.User).delete()
        db.commit()
        db.close()    


def test_create_user():
    unique_username = f"testuser_{uuid.uuid4().hex[:8]}"
    unique_email = f"{uuid.uuid4()}@example.com"

    response = client.post("/users/", json={
        "username": unique_username,
        "email": unique_email,
        "password": "test1234"
    })

    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["username"] == unique_username
    assert data["email"] == unique_email

def test_list_users():
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

