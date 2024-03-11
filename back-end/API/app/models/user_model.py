from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), default=False)
    admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.password}',  '{self.admin}')"
    
    def to_json_string(self):
        return {'id': self.id, 'name': self.name, 'email': self.email, 'password': self.password, 'admin': self.admin}