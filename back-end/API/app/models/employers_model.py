from app import db

class Employers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    verified = db.Column(db.boolean, nullable=False)
    userId = db.Column(db.integer, nullable=True)
    entrepriseId = db.Column(db.integer, nullable=False)

    def __repr__(self):
        return f"Employers(id={self.id}, verified={self.verified}, userId={self.userId}, entrepriseId={self.entrepriseId})"
    
    def to_json_string(self):
        return {
            'id': self.id,
            'verified': self.verified,
            'userId': self.userId,
            'entrepriseId': self.entrepriseId
        }