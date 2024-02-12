from flask import jsonify, request
from app import app
from app.services.user_service import UserService
user_service = UserService()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    token = user_service.login(email, password)
    if token:
        return jsonify({'token': token})
    else:
        return jsonify({'message': 'Invalid email or password'}), 401