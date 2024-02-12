from app.models.user_model import User
from app import db
from app.repositories.user_repo import UserRepo
user_repo = UserRepo()

class UserService:
    def login(self, email, password):
        return user_repo.loginUser(email, password)