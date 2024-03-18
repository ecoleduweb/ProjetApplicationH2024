from app.models.jobOffer_model import JobOffer
from app import db
from app.repositories.jobOffer_repo import JobOfferRepo
jobOffer_repo = JobOfferRepo()

class JobOfferService:

    def createJobOffer(self, data):
        return jobOffer_repo.createJobOffer(data)

