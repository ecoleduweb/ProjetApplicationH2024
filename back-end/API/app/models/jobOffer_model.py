from app import db

class JobOffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    dateEntryOffice = db.Column(db.dynamic_loaderate, nullable=False)
    deadlineApply = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    hoursPerWeek = db.Column(db.Double, nullable=False)
    compliantEmploymentStandards = db.Column(db.Boolean, nullable=False)
    internship = db.Column(db.Boolean, nullable=False)
    offerStatus = db.Column(db.Integer, nullable=False)
    offerLink = db.Column(db.String(255), nullable=False)
    urgent = db.Column(db.Boolean, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    employerId = db.Column(db.Integer, nullable=False)
    scheduleId = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"JobOffer('{self.title}', '{self.address}', '{self.description}', '{self.dateEntryOffice}', '{self.deadlineApply}', '{self.email}', '{self.hoursPerWeek}', '{self.compliantEmploymentStandards}', '{self.internship}', '{self.offerStatus}', '{self.offerLink}', '{self.urgent}', '{self.active}', '{self.employerId}', '{self.scheduleId}')"
    
    def to_json_string(self):
        return {'id': self.id, 'title': self.title, 'address': self.address, 'description': self.description, 'dateEntryOffice': self.dateEntryOffice, 'deadlineApply': self.deadlineApply, 'email': self.email, 'hoursPerWeek': self.hoursPerWeek, 'compliantEmploymentStandards': self.compliantEmploymentStandards, 'internship': self.internship, 'offerStatus': self.offerStatus, 'offerLink': self.offerLink, 'urgent': self.urgent, 'active': self.active, 'employerId': self.employerId, 'scheduleId': self.scheduleId}