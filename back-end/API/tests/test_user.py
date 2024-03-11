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
from app.repositories.user_repo import UserRepo
user_repo = UserRepo()
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


class TestUserRepo(BaseTestCase):
    def test_createUser(self):
        with self.app.app_context():
            user = user_repo.createUser({"name": "test", "email": "test@gmail.com", "password": "test"})
            self.assertEqual(user.name, "test")



if __name__ == '__main__':
    unittest.main()