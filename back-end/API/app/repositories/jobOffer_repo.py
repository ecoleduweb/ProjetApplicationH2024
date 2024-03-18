from app import db
from app.models.jobOffer_model import JobOffer
from flask import Flask, jsonify

class JobOfferRepo:

    def createJobOffer(self, data):
        new_job_offer = JobOffer(**data)
        db.session.add(new_job_offer)
        db.session.commit()
        return jsonify({'message': 'new job offer created'})

    def offreEmploi(self, id):
        jobOffer = JobOffer.query.filter_by(id=id).first()
        return jobOffer

    def offresEmploi(self):
        jobOffers = JobOffer.query.all()
        return jobOffers