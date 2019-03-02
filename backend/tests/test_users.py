import json
import pytest


def test_api(client):
    resp = client.get('/api')
    assert resp.status_code == 200
    assert json.loads(resp.data) == {
        "message": "Hello"
    }

@pytest.mark.usefixtures('_db')
def test_users(client, user_factory):
    user1 = user_factory('test', 'test@example.com')
    user2 = user_factory('test2', 'test2@example.com')
    resp = client.get('/api/users')
    assert resp.status_code == 200
    assert json.loads(resp.data) == [
        {},
        {},
    ]
