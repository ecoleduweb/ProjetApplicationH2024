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
            jobOffer_data['EmployerId'] = jobOffer.EmployerId
            jobOffer_data['ScheduleId'] = jobOffer.ScheduleId
            output.append(jobOffer_data)
        return jsonify({'jobOffers': output})

    def getJobOffer(self, id):
        return JobOffer.query.filter_by(id=id).first()

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