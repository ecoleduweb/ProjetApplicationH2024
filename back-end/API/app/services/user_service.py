from app.models.user_model import User
from app import db
from flask import jsonify
from argon2 import PasswordHasher
import datetime
from jwt import encode
import os
from app.repositories.auth_repo import AuthRepo
auth_repo = AuthRepo()

hasher = PasswordHasher()

class UserService:
    def login(self, data):
        email = data['email']
        user = auth_repo.getUser(email)
        isvalid = hasher.verify(user.password, data['password'])
        if not user:
            return jsonify({'message': 'user not found'})
        elif isvalid:
            token = encode({'email': user.email, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, os.environ.get('SECRET_KEY'))
            return jsonify({'token' : token})
        return jsonify({'message': 'could not verify'})
    
    def createUser(self, data):
        return auth_repo.createUser(data)

    def getAllUsers(self):
        return auth_repo.getAllUsers()
    
    def getUser(self, email):
        return auth_repo.getUser(email)
    
    def updatePassword(self, data):
        return auth_repo.updatePassword(data)