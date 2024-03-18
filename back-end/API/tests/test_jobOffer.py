import os
import pytest
from app import create_app, db
from app.models.jobOffer_model import JobOffer
from sqlalchemy import text

# Token for authentication
TOKEN = os.environ.get('BEARER_TOKEN')

@pytest.fixture(scope='module')
def client(app):
    return app.test_client()

@pytest.fixture(scope='module')
def app():
    app = create_app()
    with app.app_context():
        db.create_all()
        job_offer1_data = {
            "id": 1,
            "title": "Développeur",
            "address": "123 rue de la rue",
            "description": "Développeur fullstack",
            "dateEntryOffice": "2021-12-12",
            "deadlineApply": "2021-12-12",
            "email": "test@gmail.com",
            "hoursPerWeek": 40,
            "compliantEmployer": True,
            "internship": False,
            "offerStatus": 1,
            "offerLink": "www.google.com",
            "urgent": False,
            "active": True,
            "employerId": 1,
            "scheduleId": 1
        }
        job_offer = JobOffer(**job_offer1_data)
        db.session.add(job_offer)
        job_offer2_data = {
            "id": 2,
            "title": "Développeur",
            "address": "123 rue de la rue",
            "description": "Développeur front-end",
            "dateEntryOffice": "2021-12-12",
            "deadlineApply": "2021-12-12",
            "email": "test@gmail.com",
            "hoursPerWeek": 40,
            "compliantEmployer": True,
            "internship": False,
            "offerStatus": 1,
            "offerLink": "www.google.com",
            "urgent": False,
            "active": True,
            "employerId": 1,
            "scheduleId": 1
        }
        job_offer2 = JobOffer(**job_offer2_data)
        db.session.add(job_offer2)
        db.session.commit()
        yield app
        db.session.remove()
        db.drop_all()


def test_offreEmploi(client):
    response = client.get('/jobOffer/offreEmploi?id=1')
    print(response)
    assert response.status_code == 200
    assert response.json == {
        "id": 1,
        "title": "Développeur",
        "address": "123 rue de la rue",
        "description": "Développeur fullstack",
        "dateEntryOffice": "2021-12-12",
        "deadlineApply": "2021-12-12",
        "email": "test@gmail.com",
        "hoursPerWeek": 40,
        "compliantEmployer": True,
        "internship": False,
        "offerStatus": 1,
        "offerLink": "www.google.com",
        "urgent": False,
        "active": True,
        "employerId": 1,
        "scheduleId": 1
    }

def test_offresEmploi(client):
    response = client.get('/jobOffer/offresEmploi')
    print(response)
    assert response.status_code == 200
    assert len(response.json) == 2
