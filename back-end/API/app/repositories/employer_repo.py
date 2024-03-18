from app import db
from app.models.employers_model import Employers
from flask import jsonify

class EmployerRepo:
    def createEmployer(self, data):
        employer = Employers(data['userId'], data['enterpriseId'], data['verified'])
        db.session.add(employer)
        db.session.commit()
        return (employer, jsonify({'message': 'new employer created'}), 201)
    
    def linkEmployerEnterprise(self, data):
        employer = Employers.query.filter_by(user_id=data['userId']).first()
        employer.enterprise_id = data['enterpriseId']
        db.session.commit()
        return jsonify({'message': 'employer linked to enterprise'})
