from app import db
from app.models.jobOffer_model import JobOffer
from flask import Flask, jsonify


class JobOfferRepo:

    def createJobOffer(self, data):
        new_job_offer = JobOffer(**data)
        db.session.add(new_job_offer)
        db.session.commit()
        return jsonify({'message': 'new job offer created'})

    def getAllJobOffers(self):
        return JobOffer.query.all()

    def getJobOffer(self, title):
        return JobOffer.query.filter_by(title=title).first()

    def updateJobOffer(self, data):
        job_offer = JobOffer.query.get(data['id'])
        if job_offer:
            for key, value in data.items():
                setattr(job_offer, key, value)
            db.session.commit()
        return jsonify({'message': 'job offer updated'})

    def deleteJobOffer(self, id):
        job_offer = JobOffer.query.get(id)
        if job_offer:
            db.session.delete(job_offer)
            db.session.commit()
            return job_offer
        return None