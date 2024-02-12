import os
import unittest
from flask_testing import TestCase
from pathlib import Path
import sys
from dotenv import load_dotenv

load_dotenv()

current_file = Path(__file__).resolve()
parent_directory = current_file.parent
project_directory = parent_directory.parent

sys.path.append(str(project_directory))

from app import app, db
from app.services.user_service import UserService
user_service = UserService()
from app.models.user_model import User

class BaseTestCase(TestCase):
    def create_app(self):
        app.config['TEST'] = "true"
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_TEST_URL")
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestUserService(BaseTestCase):
    def test_getAllUser(self):
        with self.app.app_context():
            users = user_service.getAllUser()
            self.assertEqual(len(users), 0)

class TestUserController(BaseTestCase):
    def test_getAllUser_route(self):
        response = self.client.get('/getAllUsers')
        result = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', result)

if __name__ == '__main__':
    unittest.main()