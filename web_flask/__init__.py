#!/usr/bin/python3
"""
initialization file
"""
from flask import Flask


def create_app():
    """
    Create the app
    """
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'mykey'

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
