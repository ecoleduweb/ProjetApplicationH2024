from app import db
from app.models.employers_model import Employers
from flask import jsonify

class EmployerRepo:
    def createEmployer(self, data):
        employer = Employers(data['name'], data['email'], data['phone'], data['address'], data['cityId'])
        db.session.add(employer)
        return (employer, jsonify({'message': 'new employer created'}), 201)
