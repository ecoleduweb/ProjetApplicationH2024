from app import db

class Employers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.integer, nullable=False)
    userId = db.Column(db.integer, nullable=False)
    entrepriseId = db.Column(db.integer, nullable=False)

    def __repr__(self):
        return f"Employers('{self.task}')"