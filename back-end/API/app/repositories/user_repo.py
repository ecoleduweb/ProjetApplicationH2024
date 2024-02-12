from app import db, app
from app.models.user_model import User
from flask import Flask, jsonify, request, make_response
from functools import wraps
import os
from werkzeug.security import generate_password_hash, check_password_hash

import datetime

import uuid

import jwt


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

class UserRepo:

    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')
            if 'Authorization' in request.headers:
                token = request.headers['Authorization']
            if not token:
                return jsonify({'message': 'a valid token is missing'})

            try:
                data = decode(token, app.config['SECRET_KEY'])
                current_user = User.query.filter_by(public_id=data['public_id']).first()
            except:
                return jsonify({'message': 'token is invalid'})

            return f(current_user, *args, **kwargs)
        return decorated


    def getAllUsers(self):
        return User.query.all()

    def login():
        auth = request.authorization

        if auth and auth.password == 'password':
            token = jwt.encode({'user': auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return jsonify({'token' : token.decode('UTF-8')})

        return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

    @token_required
    def createUser(self, user):
        db.session.add(user)
        db.session.commit()
        return user
    