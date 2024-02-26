import os
import pytest
from argon2 import PasswordHasher
from app import create_app
from app.models.user_model import db, User

hasher = PasswordHasher()

@pytest.fixture(scope='module')
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
        hashed_password = hasher.hash("phil123")
        user = User(name="Phil", email="philsaucier@gmail.com", password=hashed_password, admin=False)
        db.session.add(user)
        db.session.commit()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    return app.test_client()

def test_createUser(client):
    data = {
        "name": "Phil",
        "email": "phil@gmail.com",
        "password": "phil123",
        "admin": False 
    }
    response = client.post('/createUser', json=data)
    assert response.status_code == 200

def test_login(client):
    data = {
        "email": "philsaucier@gmail.com",
        "password": "phil123"
    }
    response = client.post('/login', json=data)
    assert response.status_code == 200
    assert 'token' in response.json
