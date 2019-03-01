from flask_sqlalchemy import SQLAlchemy
from webargs.flaskparser import FlaskParser


db = SQLAlchemy()
webargs = FlaskParser()
