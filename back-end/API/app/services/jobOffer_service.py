from app.models.jobOffer_model import JobOffer
from app import db
from app.repositories.jobOffer_repo import JobOfferRepo
jobOffer_repo = JobOfferRepo()

class UserService:
    def login(self, data):
        return jobOffer_repo.login(data)
    
    def createJobOffer(self, data):
        return jobOffer_repo.createUser(data)

    def getAllJobOffer(self):
        return jobOffer_repo.getAllUsers()
    
    def getJobOffer(self, title):
        return jobOffer_repo.getUser(title)
    
    def updateJobOffer(self, data):
        return jobOffer_repo.updateJobOffer(data)
    
    def deleteJobOffer(self, id):
        return jobOffer_repo.deleteJobOffer(id)