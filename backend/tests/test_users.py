import json

import pytest

from .utils.equals import EqualsUUIDString


def test_api(client):
    resp = client.get("/api")
    assert resp.status_code == 200
    assert json.loads(resp.data) == {"message": "Hello"}


@pytest.mark.usefixtures("db_session")
def test_users(client, user_factory):
    user1 = user_factory("test", "test@example.com")
    user2 = user_factory("test2", "test2@example.com")
    resp = client.get("/api/users/")
    assert resp.status_code == 200

    assert json.loads(resp.data) == {
        "data": [
            {"id": str(user1.id), "username": user1.username, "email": user1.email},
            {"id": str(user2.id), "username": user2.username, "email": user2.email},
        ]
    }


@pytest.mark.usefixtures("db_session")
def test_user_create(client):
    data = {"username": "test", "email": "test@example.com"}
    resp = client.post(
        "/api/users/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )
    assert resp.status_code == 201
    assert json.loads(resp.data) == {
        "data": {
            "username": "test",
            "email": "test@example.com",
            "id": EqualsUUIDString(),
        }
    }


@pytest.mark.usefixtures("db_session")
def test_user_update(client, user_factory):
    user = user_factory("name", "name@example.com")
    data = {"username": "nameNew", "email": "name.new@example.com"}
    resp = client.post(
        f"/api/users/{user.id}",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )
    assert resp.status_code == 200

    assert json.loads(resp.data) == {
        "data": {
            "id": str(user.id),
            "username": "nameNew",
            "email": "name.new@example.com",
        }
    }


@pytest.mark.usefixtures("db_session")
def test_user_delete(client, user_factory):
    user = user_factory("name", "name@example.com")
    resp = client.delete(f"/api/users/{user.id}")
    assert resp.status_code == 200

    assert json.loads(resp.data) == {
        "data": {"id": str(user.id), "username": "name", "email": "name@example.com"}
    }
