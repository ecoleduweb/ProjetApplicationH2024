from app.repositories.enterprise_repo import EnterpriseRepo
enterprise_repo = EnterpriseRepo()

class EnterpriseService:
    def createEnterprise(self, data, isTemporary):
        return enterprise_repo.createEnterprise(data, isTemporary)
    
    def getEnterprise(self, id):
        return enterprise_repo.getEnterprise(id)
    
    def updateEnterprise(self, data):
        return enterprise_repo.updateEnterprise(data)
    
