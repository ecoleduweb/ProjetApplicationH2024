from flask import jsonify, request, Blueprint
from app.models.user_model import User
import os
from jwt import encode, decode
from flask import Flask, jsonify, request, make_response
from functools import wraps
from app.services.jobOffer_service import JobOfferService
jobOffer_service = JobOfferService()

app_blueprint = Blueprint('app', __name__) ## Représente l'app, https://flask.palletsprojects.com/en/2.2.x/blueprints/

def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')
            if 'Authorization' in request.headers:
                token = request.headers['Authorization']
            if not token:
                return jsonify({'message': 'a valid token is missing'})

            try:
                data = decode(token, os.environ.get('SECRET_KEY'), algorithms=["HS256"])
                current_user = User.query.filter_by(email = data['email']).first()

            except Exception as e:
                print(e)
                return jsonify({'message': 'token is invalid'})
            return f(current_user)
        return decorated

@token_required
@app_blueprint.route('/offreEmploi', methods=['GET'])
def offreEmploi():
    data = request.get_json()
    return jobOffer_service.offreEmploi(data)

@token_required
@app_blueprint.route('/offresEmploi', methods=['GET'])
def offresEmploi():
    data = request.get_json()
    return jobOffer_service.offresEmploi(data)