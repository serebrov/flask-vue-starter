from app.extensions import db
from app.models.forum import User
from marshmallow import Schema, fields, ValidationError


def unique_username(username):
    query = db.session.query(User)
    query = query.filter_by(username=username)
    if query.first(): 
        raise ValidationError(
            'Username should be unique: {}'.format(username))


def unique_email(email):
    query = db.session.query(User)
    query = query.filter_by(email=email)
    if query.first(): 
        raise ValidationError(
            'Email should be unique: {}'.format(email))


class UserSchema(Schema):
    username = fields.Str(required=True, validate=unique_username)
    email = fields.Email(required=True, validate=unique_email)


class PostSchema(Schema):
    user = fields.Nested(UserSchema, attribute='created_by_user_id')
    title = fields.Str()
    text = fields.Str()
