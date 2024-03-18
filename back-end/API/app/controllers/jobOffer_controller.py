from flask import jsonify, request, Blueprint
from app.models.jobOffer_model import JobOffer
import os
from app.models.user_model import User
import os
from jwt import encode, decode
from flask import Flask, jsonify, request, make_response
from functools import wraps
from app.services.jobOffer_service import JobOfferService
jobOffer_service = JobOfferService()

job_offer_blueprint = Blueprint('job_offer', __name__) ## Représente l'app, https://flask.palletsprojects.com/en/2.2.x/blueprints/

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
      
@app_blueprint.route('/createJobOffer', methods=['POST'])
def createJobOffer():
    data = request.get_json()
    return jobOffer_service.createJobOffer(data)

@job_offer_blueprint.route('/offreEmploi', methods=['GET'])
def offreEmploi():
    id = request.args.get('id')
    jobOffer = jobOffer_service.offreEmploi(id)
    if jobOffer:
        return jsonify(jobOffer.to_json_string())
    else:
        return jsonify({'message': 'offre d\'emploi non trouvée'}), 404

@job_offer_blueprint.route('/offresEmploi', methods=['GET'])
def offresEmploi():
    jobOffers = jobOffer_service.offresEmploi()
    return jsonify([jobOffer.to_json_string() for jobOffer in jobOffers])