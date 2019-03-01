from flask import Flask
from flask_cors import CORS

from app.config import config
from app.extensions import (
    db,
    webargs,
)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    CORS(app, resources={r"/api/*": {"origins": "*"}})
    return app
