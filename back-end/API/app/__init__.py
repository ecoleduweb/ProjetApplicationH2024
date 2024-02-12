import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import pytest
import pymysql

pymysql.install_as_MySQLdb()
load_dotenv()

app = Flask(__name__)

if any("pytest" in arg for arg in sys.argv):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_TEST_URL')
    print("Running in test mode.")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_DEV_URL')
    print("Running in development mode.")

db = SQLAlchemy(app)

from app.controllers.user_controller import *

if any("pytest" in arg for arg in sys.argv):
    pytest.main(['tests/'])
