import os
from flask import Flask, jsonify, request
from marshmallow import ValidationError

from app.config import config
from app.models.forum import User
from app.serializers.forum import UserSchema

from app.extensions import (
    db,
    webargs,
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


@app.route("/user", methods=['POST'])
def user_create():
    result = webargs.parse(UserSchema(), request)

    username = result.get('username')
    email = result.get('email')

    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    schema = UserSchema()
    return jsonify(schema.dump(obj=user)), 201


@webargs.error_handler
def handle_error(error, req, schema, status_code, headers):
    raise ValidationError(error.messages)


@app.errorhandler(ValidationError)
def validateion_error(error):
    return jsonify({
        "errors": error.messages
    }), 400


@app.cli.command('db_create_all')
def db_create_all():
    db.create_all()
