from flask import jsonify, request, Blueprint
import os
from app.models.user_model import User
from app.models.employers_model import Employers
from app.models.enterprise_model import Enterprise
import os
from jwt import decode
from flask import jsonify, request
from functools import wraps
from app.services.jobOffer_service import JobOfferService
jobOffer_service = JobOfferService()
from app.services.employer_service import EmployerService
employer_service = EmployerService()
from app.services.enterprise_service import EnterpriseService
enterprise_service = EnterpriseService()
from app.services.user_service import UserService
user_service = UserService()

job_offer_blueprint = Blueprint('jobOffer', __name__) ## Représente l'app, https://flask.palletsprojects.com/en/2.2.x/blueprints/

token = os.environ.get('BEARER_TOKEN')

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
@job_offer_blueprint.route('/createJobOffer', methods=['POST'])
def createJobOffer():
    data = request.get_json()
    token = request.headers.get('Authorization')
    decoded_token = decode(token, os.environ.get('SECRET_KEY'), algorithms=["HS256"])
    user = User.query.filter_by(email = decoded_token['email']).first()
    if user.isModerator:
        return jobOffer_service.createJobOffer(data["jobOffer"])
    else:
        employer = Employers.query.filter_by(userId=user.id).first()
        if employer is None:
            entreprise = enterprise_service.createEnterprise(data["enterprise"], True)
            newEmployer = employer_service.createEmployer(entreprise.id, user.id)
            return jobOffer_service.createJobOffer(data["jobOffer"], newEmployer.id)
        else:
            return jobOffer_service.createJobOffer(data["jobOffer"], employer.id)

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

@token_required
@job_offer_blueprint.route('/linkJobOfferEmployer', methods=['PUT'])
def linkJobOfferEmployer():
    data = request.get_json()
    return jobOffer_service.linkJobOfferEmployer(data)
