from typing import Any, Optional
from uuid import UUID

from app.utils.types import JSON
from marshmallow import Schema, ValidationError, post_dump, validate


class WrapDataSchema(Schema):
    """Wraps data into {"data" : ...} envelop."""

    @post_dump(pass_many=True)
    def wrap_with_envelope(self, data: JSON, many: bool) -> JSON:
        """Wrap the `data` into envelop if wrap_data is True."""
        if self.wrap_data is True:
            # metadata = {}
            # if "current_user" in g and g.current_user:
            #     from app.auth.serializers import UserSchema

            #     user = UserSchema().dump(g.current_user)
            #     metadata["user"] = user
            # return {"data": data, "metadata": metadata}
            return {"data": data}
        return data

    def __init__(self, wrap_data: bool = True, *args: Any, **kwargs: Any):
        """Constructor.

        Args:
            wrap_data: default is True, set to False (default) to
              disable data wrapping.
              Useful in the case when the same schema is used on
              the top level in the response and as a nested
              schema in another response (here we don't need to
              wrap it).
        """
        self.wrap_data = wrap_data
        super().__init__(*args, **kwargs)


class UUIDFormat(validate.Validator):
    """Validator which succeeds if the value passed to it is
    a valid UUID string.
    """

    message = "Not a valid UUID"

    def __init__(self, error: Optional[str] = None):
        self.error = error

    def _format_error(self, value: Any, message: str) -> str:
        return (self.error or message).format(input=value)

    def __call__(self, value: Any) -> Any:
        if type(value) != str and type(value) != UUID:
            raise ValidationError(self._format_error(value, self.message))

        if type(value) == str:
            try:
                UUID(value)
            except ValueError:
                raise ValidationError(self._format_error(value, self.message))

        return value


"""Validator to check that the field is not blank."""
not_blank = validate.Length(min=1, max=10000, error="Field cannot be blank")

"""Validator to check that the field is valid UUID."""
uuid_format = UUIDFormat()
