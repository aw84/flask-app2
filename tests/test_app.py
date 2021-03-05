import json

import pytest
from app import create_app
from app.model.User import User


@pytest.fixture
def app():
    app = create_app('TEST')
    yield app


@pytest.fixture
def client(app):
    with app.app_context() as c:
        from app.model import db
        try:
            db.create_all()
            yield app.test_client()
        finally:
            db.session.remove()
            db.drop_all()


def test_config():
    assert create_app('TEST').testing
    assert create_app('DEV').debug


def test_user_create(client):
    data = {
        'user': 'test',
        'email': 'abcd'
    }
    response = client.post("/api/User", json=data, follow_redirects=True)
    assert response.status_code == 200
    assert json.loads(response.data)['user'] == data['user']
    assert json.loads(response.data)['email'] == data['email']

    u = User.query.filter(User.username == data['user']).first()
    assert u is not None


def test_send_msg(client):

    sender_token = 'sender secret'

    authorization_headers = {
        'x-auth-token': sender_token
    }

    data = {
        'recipient': '11',
        'group': '123',
        'msg': 'test message'
    }

    response = client.post('/api/msg', json=data,
                           headers=authorization_headers,
                           follow_redirects=True)

    assert response.status_code == 200


def test_get_msg(client):

    recipient_token = 'recpient secret'

    authorization_headers = {
        'x-auth-token': recipient_token
    }

    response = client.get('/api/msg', json=data,
                          headers=authorization_headers,
                          follow_redirects=True)

    assert response.status_code == 200
