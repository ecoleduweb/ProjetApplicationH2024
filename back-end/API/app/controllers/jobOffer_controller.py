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
