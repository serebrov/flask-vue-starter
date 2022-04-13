from app.config import config
from app.extensions import api, init_app_extensions, webargs
from flask import Flask, jsonify
from flask_cors import CORS
from marshmallow import ValidationError
from typing import Any

from .cli import register_cli_handlers

# from app.auth.authentication import basic_auth


def register_api(app: Flask) -> None:
    """Register blueprints and routes."""
    from app.forum.api import blueprint as forum_blueprint
    from app.user.api import blueprint as user_blueprint

    api.register_blueprint(user_blueprint)
    api.register_blueprint(forum_blueprint)

    @app.route("/api")
    def hello() -> Any:
        return jsonify({"message": "Hello"})


def register_api_error_handlers(app: Flask) -> None:
    """Register error handlers for API.

    These are generic handlers that apply to all API requests.
    """

    @webargs.error_handler
    def handle_error(
        error, req, schema, error_status_code, error_headers
    ):  # type: ignore
        if "json" in error.messages:
            raise ValidationError(error.messages["json"])
        if "path" in error.messages:
            raise ValidationError(error.messages["path"])
        raise ValidationError(error.messages)

    @app.errorhandler(ValidationError)
    def validateion_error(error):  # type: ignore
        return jsonify({"errors": error.normalized_messages()}), 400

    # @basic_auth.error_handler
    # def error_handler(*args, **kwargs):  # type: ignore
    #     return jsonify({"error": "Unauthorized"}), 401


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    init_app_extensions(app)

    # Note: unsafe, better set origins to known hosts
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Register API methods.
    register_api(app)
    # Register error handlers.
    register_api_error_handlers(app)
    # Register cli commands.
    register_cli_handlers(app)
    # Init flask admin - disabled for now as it doesn't have
    # authentication, so we can't have it like this on develop/production
    # also, it is not usable for now
    # init_admin(app)
    return app
