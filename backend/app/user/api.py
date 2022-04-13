"""User API."""
from app.extensions import db
from app.utils.types import JSON
from flask_smorest import Blueprint, abort

from .models import User
from .serializers import UserSchema

blueprint = Blueprint(
    "users", "users", url_prefix="/api/users", description="Operations on users"
)


@blueprint.route("/", methods=["GET"])
@blueprint.response(200, UserSchema(many=True))
def users_get():
    return User.query.all()


@blueprint.route("/<string:id>", methods=["GET"])
@blueprint.response(200, UserSchema())
def user_get(id: str):
    user = User.query.get(id)
    if user is None:
        abort(404, message="User not found.")
    return user


@blueprint.route("/", methods=["POST"])
@blueprint.arguments(UserSchema())
@blueprint.response(201, UserSchema())
def user_create(user_data: JSON):
    user = User(**user_data)
    db.session.add(user)
    db.session.commit()
    return user


@blueprint.route("/<string:id>", methods=["POST"])
@blueprint.arguments(UserSchema())
@blueprint.response(200, UserSchema())
def user_update(user_data: JSON, id: str):
    user = User.query.get(id)
    if not user:
        abort(404, message="User not found.")

    # Assign validated attributes to the model.
    for attr, value in user_data.items():
        setattr(user, attr, value)

    db.session.add(user)
    db.session.commit()
    return user


@blueprint.route("/<string:id>", methods=["DELETE"])
@blueprint.response(200, UserSchema())
def user_delete(id: str):
    user = User.query.get(id)
    if not user:
        abort(404, message="User not found.")

    db.session.delete(user)
    db.session.commit()
    return user
