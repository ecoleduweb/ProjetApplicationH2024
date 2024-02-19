from app.models.user_model import User
from app import db
from app.repositories.user_repo import UserRepo
user_repo = UserRepo()

class UserService:
    def login(self, data):
        return user_repo.login(data)
    
    def createUser(self, data):
        return user_repo.createUser(data)

    def getAllUsers(self):
        return user_repo.getAllUsers()
    
    def getUser(self, email):
        return user_repo.getUser(email)
    
    def updatePassword(self, data):
        return user_repo.updatePassword(data)