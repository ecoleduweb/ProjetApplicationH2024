from app import db

class Entreprise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    cityId = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User('{self.task}')"