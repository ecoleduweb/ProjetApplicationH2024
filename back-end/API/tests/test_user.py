import os
import pytest
from dotenv import load_dotenv
from app import create_app

load_dotenv()

@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.config['TESTING'] = True  # Activer le mode test
    yield app

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
