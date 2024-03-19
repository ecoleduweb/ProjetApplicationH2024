import sys
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import pymysql
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from logging.config import dictConfig

dictConfig({
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
        },
        "simpleformatter": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
        },
    },
    "handlers": {
        "wsgi": {"class": "logging.StreamHandler", "formatter": "default"},
        "custom_handler": {
            "class": "logging.FileHandler",
            "formatter": "simpleformatter",
            "filename": "logs.txt",
            "level": "WARN",
        },
    },
    "root": {"level": "INFO", "handlers": ["wsgi", "custom_handler"]},
}
)
SWAGGER_URL_PREFIX = "/swagger"
SWAGGER_LOCATION = "/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL_PREFIX,
    SWAGGER_LOCATION,
    config={"app_name": "Gestion de demandes d'emplois"},
)

db = SQLAlchemy()

pymysql.install_as_MySQLdb()
load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    CORS(app, origins=['http://10.172.80.144', 'http://localhost', 'http://134.122.45.61', 'http://134.122.37.198', 'http://68.183.200.68'])

    try:
        if any("pytest" in arg for arg in sys.argv):
            app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_TEST_URL")
        else:
            app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_DEV_URL")
            print("Running in development mode.")
    except Exception as e:
        print(e)
        print("Error loading environment variables.")
        return jsonify({"message": "Error loading environment variables"}), 500

    db.init_app(app)

    from app.controllers.user_controller import app_blueprint as user_blueprint
    app.register_blueprint(user_blueprint)

    from app.controllers.ping_controller import ping_blueprint
    app.register_blueprint(ping_blueprint)

    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL_PREFIX)

    return app
