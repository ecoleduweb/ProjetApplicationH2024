from app import db
from app.models.jobOffer_model import JobOffer
from flask import jsonify

class JobOfferRepo:
    def offreEmploi(self, id):
        jobOffer = JobOffer.query.filter_by(id=id).first()
        return jobOffer

    def offresEmploi(self):
        jobOffers = JobOffer.query.all()
        return jobOffers
