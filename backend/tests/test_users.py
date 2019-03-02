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
    print(json.loads(resp.data))
    assert json.loads(resp.data) == {'data': [
        {'id': str(user1.id), 'username': user1.username, 'email': user1.email},
        {'id': str(user2.id), 'username': user2.username, 'email': user2.email},
    ]}
