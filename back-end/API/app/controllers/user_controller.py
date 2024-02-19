from flask import jsonify, request, Blueprint
from app.models.user_model import User
import os
from jwt import encode, decode
from flask import Flask, jsonify, request, make_response
from functools import wraps
from app.services.user_service import UserService
user_service = UserService()

app_blueprint = Blueprint('app', __name__)

def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')
            if 'Authorization' in request.headers:
                token = request.headers['Authorization']
            if not token:
                return jsonify({'message': 'a valid token is missing'})

            try:
                data = decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
                current_user = User.query.filter_by(email = data['email']).first()

            except Exception as e:
                print(e)
                return jsonify({'message': 'token is invalid'})
            return f(current_user)
        return decorated

@app_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return user_service.login(data)

@app_blueprint.route('/createUser', methods=['POST'])
def createUser():
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({'message': 'Invalid JSON data format'}), 400
    
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    
    if not all([name, email, password]):
        return jsonify({'message': 'Missing required fields'}), 400
    
    return user_service.createUser(data)

@app_blueprint.route('/updatePassword', methods=['PUT'])
@token_required
def updatePassword(current_user):
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({'message': 'Invalid JSON data format'}), 400
    email = data.get('email')
    password = data.get('password')
    
    if not all([email, password]):
        return jsonify({'message': 'Missing required fields'}), 400
    return user_service.updatePassword(data)

@app_blueprint.route('/getAllUsers', methods=['GET'])
@token_required
def getAllUsers(current_user):
    return user_service.getAllUsers()

@app_blueprint.route('/getUser', methods=['GET'])
@token_required
def getUser(current_user):
    email = request.args.get('email')
    if not email:
        return jsonify({'message': 'Missing required fields'}), 400
    return user_service.getUser(email)
