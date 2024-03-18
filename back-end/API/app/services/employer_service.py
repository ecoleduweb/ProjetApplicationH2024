from app.repositories.employer_repo import EmployerRepo
employer_repo = EmployerRepo()

class EmployerService:
    def createEmployer(self, data):
        return employer_repo.createEmployer(data)
