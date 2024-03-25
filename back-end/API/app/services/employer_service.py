from app.repositories.employer_repo import EmployerRepo
from app.repositories.enterprise_repo import EnterpriseRepo
employer_repo = EmployerRepo()
enterprise_repo = EnterpriseRepo()
class EmployerService:
    def createEmployer(self, enterpriseId, userId):
        return employer_repo.createEmployer(enterpriseId, userId)

    def linkEmployerEnterprise(self, data):
        employer_repo.linkEmployerEnterprise(data)
        enterprise_repo.deleteEnterprise(data['enterpriseId'])
    # vérifier si l'employeur est validé
    # vérifier si l'entreprise est temporaire
    # supprimer si entreprise existe déjà