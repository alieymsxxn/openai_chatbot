from flask import Blueprint

# Blueprint for the OpenAI chatbot module
# This blueprint will handle all routes related to the OpenAI chatbot functionality.
blueprint = Blueprint('openai', __name__)

from . import routes