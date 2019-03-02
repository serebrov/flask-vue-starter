from app.extensions import db
from app.models.forum import User
from marshmallow import Schema, fields, validates_schema, ValidationError


def validate_unique_field(name, value, id=None):
    query = User.query.filter(getattr(User, name) == value)
    if id is not None:
        query = query.filter(User.id != id)
    if query.first(): 
        raise ValidationError(
            'Username should be unique: {}'.format(value), name)


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)

    @validates_schema
    def validate_unique_fields(self, data):
        id = None
        if 'user' in self.context:
            id = self.context['user'].id
        username = data.get('username')
        validate_unique_field('username', username, id)
        email = data.get('email')
        validate_unique_field('email', email, id)


class PostSchema(Schema):
    user = fields.Nested(UserSchema, attribute='created_by_user_id')
    title = fields.Str()
    text = fields.Str()
