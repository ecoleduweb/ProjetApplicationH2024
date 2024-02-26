from flask import jsonify, request
from app import app
from app.models.jobOffer_model import jobOffer
import os
from flask import Flask, jsonify, request, make_response
from functools import wraps
from app.services.jobOffer_service import jobOfferService
jobOffer_service = jobOfferService()

@app.route('/createJobOffer', methods=['POST'])
def createJobOffer():
    data = request.get_json()
    return jobOffer_service.createJobOffer(data)

@app.route('/getAllJobOffers', methods=['GET'])
def getAllJobOffers():
    return jobOffer_service.getAllJobOffers()

@app.route('/getJobOffer', methods=['GET'])
def getJobOffer(title):
    title = request.args.get('title')
    return jobOffer_service.getJobOffer(title)

@app.route('/updateJobOffer', methods=['PUT'])
def updateJobOffer(id):
    data = request.get_json()
    data['id'] = id
    return jobOffer_service.updateJobOffer(data)

@app.route('/deleteJobOffer', methods=['DELETE'])
def deleteJobOffer(id):
    return jobOffer_service.deleteJobOffer(id)
