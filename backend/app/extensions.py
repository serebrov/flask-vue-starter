from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from webargs.flaskparser import FlaskParser
from flask_migrate import Migrate

db = SQLAlchemy()
webargs = FlaskParser()
migrate = Migrate()


def init_app_extensions(app: Flask):
    """Intitialize the extensions with app instance."""
    db.init_app(app)
    migrate.init_app(app, db)
