from flask import Blueprint
from logging import getLogger

logger = getLogger(__name__)

ping_blueprint = Blueprint('ping', __name__)

@ping_blueprint.route('/ping', methods=['GET'])
def ping():
    logger.warn('Pong')
    return "Pong!", 200