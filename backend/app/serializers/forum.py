from app.models.forum import User
from marshmallow import Schema, fields, validates_schema, ValidationError


def validate_unique_field(name, value, id=None):
    """Validate unique field.

    Args:
        name: field name to validate ('username' or 'email')
        value: value to validate
        id: optional user id, should be specified on user update

    Returns:
        Nothing, raises ValidationError if validation failed.
    """
    query = User.query.filter(getattr(User, name) == value)
    if id is not None:
        # Allow updating username or email for the user to the
        # same value.
        query = query.filter(User.id != id)
    if query.first():
        raise ValidationError("{} should be unique: {}".format(name, value), name)


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)

    @validates_schema
    def validate_unique_fields(self, data):
        """Valdiate username and email to make sure they are unique."""
        id = None
        if "user" in self.context:
            id = self.context["user"].id

        username = data.get("username")
        validate_unique_field("username", username, id)
        email = data.get("email")
        validate_unique_field("email", email, id)


class PostSchema(Schema):
    user = fields.Nested(UserSchema, attribute="created_by_user_id")
    title = fields.Str()
    text = fields.Str()
