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
    return jsonify({"data": UserSchema().dump(obj=user)}), 200


@app.route("/api/users", methods=['GET'])
def users_get():
    users = User.query.all()
    return jsonify({"data": UserSchema().dump(users, many=True)}), 200


@app.route("/api/users", methods=['POST'])
def user_create():
    result = webargs.parse(UserSchema(), request)
    user = User(**result)
    db.session.add(user)
    db.session.commit()
    return jsonify({"data": UserSchema().dump(obj=user)}), 201


@app.route("/api/users/<string:id>", methods=['POST'])
def user_update(id):
    user = User.query.get(id)
    if not user:
        raise ValidationError(
            'User not found by id: {}'.format(id), 'id')

    # Pass user as schema context, so we can do additional
    # validation based on the user data.
    schema = UserSchema()
    schema.context['user'] = user
    result = webargs.parse(schema, request)

    # Assign validated attributes to the model.
    for attr, value in result.items():
        setattr(user, attr, value)

    db.session.add(user)
    db.session.commit()
    return jsonify({"data": UserSchema().dump(obj=user)}), 201


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
