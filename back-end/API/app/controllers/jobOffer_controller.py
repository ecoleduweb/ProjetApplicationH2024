from flask import jsonify, request, Blueprint
from app.models.jobOffer_model import JobOffer
import os
from flask import Flask, jsonify, request, make_response
from functools import wraps
from app.services.jobOffer_service import JobOfferService
jobOffer_service = JobOfferService()

app_blueprint = Blueprint('app', __name__) ## Représente l'app, https://flask.palletsprojects.com/en/2.2.x/blueprints/

@app_blueprint.route('/createJobOffer', methods=['POST'])
def createJobOffer():
    data = request.get_json()
    return jobOffer_service.createJobOffer(data)


@app_blueprint.route('/getAllJobOffers', methods=['GET'])
def getAllJobOffers():
    return jobOffer_service.getAllJobOffers()

@app_blueprint.route('/getJobOffer', methods=['GET'])
def getJobOffer():
    id = request.args.get('id', type=int)
    if id is None:
        return jsonify({'message': 'Missing job offer ID'}), 400

    jobOffer_data = jobOffer_service.getJobOffer(id)
    if jobOffer_data:
        return jsonify(jobOffer_data), 200
    else:
        return jsonify({'message': 'JobOffer not found'}), 404
    
@app_blueprint.route('/updateJobOffer', methods=['PUT'])
def updateJobOffer(id):
    if not request.json:
        return jsonify({'error': 'Bad request'}), 400
    
    update_data = request.get_json()
    result = jobOffer_service.updateJobOffer(id, update_data)
    
    if result:
        return jsonify({'success': 'Job offer updated successfully'}), 200
    else:
        return jsonify({'error': 'Job offer not found'}), 404

@app_blueprint.route('/deleteJobOffer', methods=['DELETE'])
def deleteJobOffer(id):
    return jobOffer_service.deleteJobOffer(id)
