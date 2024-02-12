from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User('{self.task}')"