from app import db, app
from app.models.user_model import User
from flask import Flask, jsonify, request
from functools import wraps
from argon2 import PasswordHasher
import datetime
from jwt import encode

hasher = PasswordHasher()

class UserRepo:

    def login(self, data):
        user = User.query.filter_by(email=data['email']).first()
        isvalid = hasher.verify(user.password, data['password'])
        if not user:
            return jsonify({'message': 'user not found'})
        elif isvalid:
            token = encode({'email': user.email, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return jsonify({'token' : token})
        return jsonify({'message': 'could not verify'})

    def createUser(self, data):
        hashed_password = hasher.hash(data['password'])
        new_user = User(name=data['name'], email=data['email'], password=hashed_password, admin=False)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'new user created'})

    def updatePassword(self, data):
        user = User.query.filter_by(email=data["email"]).first()
        if not user:
            return jsonify({'message': 'no user found'})
        user.password = hasher.hash(data['password'])
        db.session.commit()
        return jsonify({'message': 'password updated'})

    def getUser(self, current_user):
        print(current_user)
        email = request.args.get('email')
        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({'message': 'no user found'})
        return jsonify({'name': user.name, 'email': user.email, 'admin': user.admin})

    def getAllUsers(self):
        users = User.query.all()
        output = []
        for user in users:
            user_data = {}
            user_data['id'] = user.id
            user_data['name'] = user.name
            user_data['email'] = user.email
            user_data['password'] = user.password
            user_data['admin'] = user.admin
            output.append(user_data)
        return jsonify({'users': output})
