from flask import Blueprint

blueprint = Blueprint('openai', __name__)

from . import routes