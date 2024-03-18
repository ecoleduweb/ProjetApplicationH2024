from app import db
from app.models.jobOffer_model import JobOffer
from flask import Flask, jsonify


class JobOfferRepo:

    def createJobOffer(self, data):
        new_job_offer = JobOffer(**data)
        db.session.add(new_job_offer)
        db.session.commit()
        return jsonify({'message': 'new job offer created'})