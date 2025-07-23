from typing import Any, Optional
from uuid import UUID

from marshmallow import Schema, ValidationError, validate


class WrapDataSchema(Schema):
    """Wraps data into {"data" : ...} envelop."""

    def dump(self, obj, *, many=None):
        """Override dump to handle wrapping correctly for both single and many cases."""
        # Get the many parameter, defaulting to the schema's many setting
        if many is None:
            many = self.many

        # Perform normal serialization first
        result = super().dump(obj, many=many)

        # Apply wrapping based on our wrap_data setting
        if self.wrap_data is True:
            return {"data": result}
        return result

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
        if type(value) is not str and type(value) is not UUID:
            raise ValidationError(self._format_error(value, self.message))

        if type(value) is str:
            try:
                UUID(value)
            except ValueError:
                raise ValidationError(self._format_error(value, self.message))

        return value


"""Validator to check that the field is not blank."""
not_blank = validate.Length(min=1, max=10000, error="Field cannot be blank")

"""Validator to check that the field is valid UUID."""
uuid_format = UUIDFormat()
