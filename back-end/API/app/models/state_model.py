from app import db

class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"User('{self.task}')"