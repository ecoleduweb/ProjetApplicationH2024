from app import db

class Province(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    province = db.Column(db.String(255), nullable=False)
    stateId = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User('{self.task}')"