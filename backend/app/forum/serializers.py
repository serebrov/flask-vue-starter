from marshmallow import Schema, fields

from app.user.serializers import UserSchema


class PostSchema(Schema):
    user = fields.Nested(UserSchema, attribute="created_by_user_id")
    title = fields.Str()
    text = fields.Str()
