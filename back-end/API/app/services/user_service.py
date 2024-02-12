from app.models.user_model import User
from app import db
from app.repositories.user_repo import UserRepo
user_repo = UserRepo()

class UserService:
    def login(self, data):
        return user_repo.login(data)
    
    def createUser(self, data):
        return user_repo.createUser(data)