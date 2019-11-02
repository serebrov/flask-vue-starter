"""Main application module.

See the actual setup in the `app.core.create_app` module.
"""
import os

from app.core.create_app import create_app


config_name = os.getenv("FLASK_CONFIG") or "local"
application = create_app(config_name)
