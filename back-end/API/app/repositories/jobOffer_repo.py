from app import db
from app.models.jobOffer_model import JobOffer
from flask import Flask, jsonify, request
from functools import wraps
from argon2 import PasswordHasher
import datetime
from jwt import encode
import os

hasher = PasswordHasher()

class JobOfferRepo:

    def offreEmploi(self, id):
        try:
            jobOffer = JobOffer.query.filter_by(id=id).first()
            if jobOffer:
                return jobOffer
            else:
                return jsonify({'message': 'job offer not found'})
        except:
            return jsonify({'message': 'error occurred'})

    def offresEmploi(self):
        jobOffers = JobOffer.query.all()
        output = []
        for jobOffer in jobOffers:
            jobOffer_data = {}
            jobOffer_data['id'] = jobOffer.id
            jobOffer_data['title'] = jobOffer.title
            jobOffer_data['address'] = jobOffer.address
            jobOffer_data['description'] = jobOffer.description
            jobOffer_data['dateEntryOffice'] = jobOffer.dateEntryOffice
            jobOffer_data['deadlineApply'] = jobOffer.deadlineApply
            jobOffer_data['email'] = jobOffer.email
            jobOffer_data['hoursPerWeek'] = jobOffer.hoursPerWeek
            jobOffer_data['compliantEmployer'] = jobOffer.compliantEmployer
            jobOffer_data['internship'] = jobOffer.internship
            jobOffer_data['offerStatus'] = jobOffer.offerStatus
            jobOffer_data['offerLink'] = jobOffer.offerLink
            jobOffer_data['urgent'] = jobOffer.urgent
            jobOffer_data['active'] = jobOffer.active
            jobOffer_data['employerId'] = jobOffer.employerId
            jobOffer_data['scheduleId'] = jobOffer.scheduleId

            output.append(jobOffer_data)
        return jsonify({'jobOffers': output})
