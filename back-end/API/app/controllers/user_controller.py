from flask import jsonify, request
from app import app
from app.services.user_service import UserService
user_service = UserService()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return user_service.login(data)

@app.route('/createUser', methods=['POST'])
def createUser():
    data = request.get_json()
    # if not isinstance(data, dict):
    #     return jsonify({'message': 'Invalid JSON data format'}), 400
    
    # name = data.get('name')
    # email = data.get('email')
    # password = data.get('password')
    
    # if not all([name, email, password]):
    #     return jsonify({'message': 'Missing required fields'}), 400
    
    return user_service.createUser(data)