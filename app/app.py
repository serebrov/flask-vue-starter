import os
from flask import Flask, jsonify
from app.config import config

from app.extensions import (
    db,
)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    return app


app = create_app(os.getenv('FLASK_CONFIG') or 'local')


@app.route("/")
def hello():
    return jsonify({
        "message": "Hello"
    })
