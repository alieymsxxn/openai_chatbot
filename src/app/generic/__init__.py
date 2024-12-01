from flask import Blueprint

# Blueprint for the generic endpoints
blueprint = Blueprint('generic', __name__)

from . import routes