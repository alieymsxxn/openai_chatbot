from flask import Flask
from app.chatbot import blueprint
import logging
from decouple import config

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = config('DEBUG', default=False, cast=bool)
    app.config['WTF_CSRF_ENABLED'] = False 

    app.register_blueprint(blueprint, url_prefix='/openai')

    return app