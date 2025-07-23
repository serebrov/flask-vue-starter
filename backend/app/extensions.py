from typing import TYPE_CHECKING
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_smorest import Api
from flask_smorest.arguments import ArgumentsMixin

db = SQLAlchemy()
migrate = Migrate()
webargs = ArgumentsMixin.ARGUMENTS_PARSER
api = Api()

# The Model is dynmaically defined in Flask-SQLAlchemy, so mypy does not recognize it.
# See https://github.com/python/mypy/issues/8603#issuecomment-1929137094
if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model
else:
    Model = db.Model


def init_app_extensions(app: Flask):
    """Initialize the extensions with app instance."""
    db.init_app(app)
    api.init_app(app)
    migrate.init_app(app, db)
