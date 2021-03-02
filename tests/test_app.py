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
            
            u1 = User(username='user1', email='user@domain.com')
            db.session.add(u1)
            db.session.commit()
            tc = app.test_client()
            yield tc
        finally:
            db.session.remove()
            db.drop_all()


def test_config():
    assert create_app('TEST').testing
    assert create_app('DEV').debug


def test_login(client):
    u = User.query.filter(User.username == 'user1').first()
    assert u is not None
    data = {
        'user': u.username,
        'pass': 'abcd'
    }
    response = client.post("/auth/login", json=data, follow_redirects=True)
    assert response.status_code == 200
    assert json.loads(response.data)['user'] == data['user']
    assert json.loads(response.data)['pass'] == data['pass']
