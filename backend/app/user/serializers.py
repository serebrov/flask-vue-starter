from uuid import UUID
from typing import Optional

from marshmallow import fields, validates_schema, ValidationError

from app.utils.serializers import WrapDataSchema
from app.utils.types import JSON
from .models import User


def validate_unique_field(
    name: str, value: Optional[str], id: Optional[UUID] = None
) -> None:
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


class UserSchema(WrapDataSchema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)

    @validates_schema
    def validate_unique_fields(self, data: JSON, partial: bool, many: bool) -> None:
        """Valdiate username and email to make sure they are unique."""
        id = None
        if "user" in self.context:
            id = self.context["user"].id

        username = data.get("username")
        validate_unique_field("username", username, id)
        email = data.get("email")
        validate_unique_field("email", email, id)
