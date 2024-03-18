from app import db
from app.models.enterprise_model import Entreprise

class EnterpriseRepo:
    def createEnterprise(self, data):
        enterprise = Entreprise(name=data['name'], email=data['email'], phone=data['phone'], address=data['address'], cityId=data['cityId'])
        db.session.add(enterprise)
        return (enterprise, {'message': 'new enterprise created'}, 200)
