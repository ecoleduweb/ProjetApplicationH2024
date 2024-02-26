from app.models.jobOffer_model import JobOffer
from app import db
from app.repositories.jobOffer_repo import JobOfferRepo
jobOffer_repo = JobOfferRepo()

class JobOfferService:

    def createJobOffer(self, data):
        return jobOffer_repo.createJobOffer(data)

    def getAllJobOffers(self):
        return jobOffer_repo.getAllJobOffers()
    
    def getJobOffer(self, title):
        return jobOffer_repo.createJobOffer(title)
    
    def updateJobOffer(self, data):
        return jobOffer_repo.updateJobOffer(data)
    
    def deleteJobOffer(self, id):
        return jobOffer_repo.deleteJobOffer(id)