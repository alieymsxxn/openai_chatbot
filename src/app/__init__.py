import logging
from flask import Flask
from .chatbot import blueprint as chatbot_blueprint
from .generic import blueprint as generic_blueprint

# Configure logging for better traceability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_app():
    '''Create and configure the Flask application.

    This function initializes the Flask app, registers the necessary blueprints,
    and prepares the app for use.

    Returns:
        Flask: The configured Flask application instance.
    '''
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['WTF_CSRF_ENABLED'] = False 

    # Register the blueprints with their respective URL prefixes
    app.register_blueprint(generic_blueprint)
    app.register_blueprint(chatbot_blueprint, url_prefix='/openai')
    logging.info('Registered chatbot blueprint with URL prefix /openai')

    return app