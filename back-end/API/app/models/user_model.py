from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), default=False)
    active = db.Column(db.Boolean, default=True)
    isModerator = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User('{self.task}')"