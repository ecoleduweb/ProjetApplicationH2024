from app.repositories.enterprise_repo import EnterpriseRepo
enterprise_repo = EnterpriseRepo()

class EnterpriseService:
    def createEnterprise(self, data):
        return enterprise_repo.createEnterprise(data)
