import os
from flask import jsonify, request
from marshmallow import ValidationError

from app.models.forum import User
from app.serializers.forum import UserSchema
from app.create_app import create_app
from app.extensions import (
    db,
    webargs,
)


app = create_app(os.getenv('FLASK_CONFIG') or 'local')


@app.route("/api")
def hello():
    return jsonify({
        "message": "Hello"
    })


@app.route("/api/user/<string:id>", methods=['GET'])
def user_get(id):
    user = User.query.get_or_404(id)
    schema = UserSchema()
    return jsonify({"data": schema.dump(obj=user)}), 200


@app.route("/api/users", methods=['GET'])
def users_get():
    users = User.query.all()
    schema = UserSchema()
    return jsonify({"data": schema.dump(users, many=True)}), 200


@app.route("/api/users", methods=['POST'])
def user_create():
    result = webargs.parse(UserSchema(), request)

    username = result.get('username')
    email = result.get('email')

    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    schema = UserSchema()
    return jsonify({"data": schema.dump(obj=user)}), 201


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
