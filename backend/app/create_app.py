from flask import Flask
from flask_cors import CORS

from app.config import config
from app.extensions import init_app_extensions


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    init_app_extensions(app)

    # Note: unsafe, better set origins to known hosts
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    return app
