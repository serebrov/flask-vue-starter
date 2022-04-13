from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_smorest import Api
from flask_smorest.arguments import ArgumentsMixin

db = SQLAlchemy()
migrate = Migrate()
webargs = ArgumentsMixin.ARGUMENTS_PARSER
api = Api()


def init_app_extensions(app: Flask):
    """Initialize the extensions with app instance."""
    db.init_app(app)
    api.init_app(app)
    migrate.init_app(app, db)
