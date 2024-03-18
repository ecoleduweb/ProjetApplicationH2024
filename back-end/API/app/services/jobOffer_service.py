from app.models.user_model import User
from app.repositories.jobOffer_repo import JobOfferRepo
jobOffer_repo = JobOfferRepo()
from app import db
from flask import jsonify
from argon2 import PasswordHasher
import datetime
from jwt import encode
import os



hasher = PasswordHasher()

class JobOfferService:
    def offreEmploi(self, data):
        return jobOffer_repo.offreEmploi(data)

    def offresEmploi(self):
        return jobOffer_repo.offresEmploi()
