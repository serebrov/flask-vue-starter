"""Flask app console commands."""
from flask import Flask

from app.extensions import db


def register_cli_handlers(app: Flask) -> None:
    """Registers helper console commands.

    Commands can be run as `flask command_name`.
    """

    @app.cli.command("db_create_all")
    def db_create_all():
        db.create_all()
