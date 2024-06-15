from flask import Flask
from flask_sqalchemy import SQAlchemy
from flask_migrate import Migrate

db = SQAlchemy()


def create_app():
    """
    Create the app
    """
    app = Flask(__name__)
    # config.Config is the file where the configuration is stored
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate = Migrage(app, db)

    from aut
