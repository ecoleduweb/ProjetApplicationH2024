from app import db
from app.models.enterprise_model import Enterprise
from flask import Flask, jsonify, request

class EnterpriseRepo:
    def createEnterprise(self, data, isTemporary):
        enterprise = Enterprise(name=data['name'], email=data['email'], phone=data['phone'], address=data['address'], cityId=data['cityId'], isTemporary=isTemporary)
        db.session.add(enterprise)
        db.session.commit()
        return enterprise

    def getEnterprise(self, id):
        try:
            enterprise = Enterprise.query.filter_by(id=id).first()
            if enterprise:
                return enterprise
            else:
                return None
        except Exception as e:
            return jsonify({'message': 'error occurred'})
    
    def updateEnterprise(self, data):
        enterprise = Enterprise.query.filter_by(id=data['id']).first()
        enterprise.name = data['name']
        enterprise.email = data['email']
        enterprise.phone = data['phone']
        enterprise.address = data['address']
        enterprise.cityId = data['cityId']
        db.session.commit()
        return enterprise
    
    def deleteEnterprise(self, id):
        enterprise = Enterprise.query.filter_by(id=id).first()
        if enterprise.isTemporary == True:
            db.session.delete(enterprise)
            db.session.commit()
        else:
            return jsonify({'message': 'enterprise is not temporary'})
        return jsonify({'message': 'enterprise deleted'})