"""Forum API."""
from flask_rest_api import Blueprint

blueprint = Blueprint(
    "forum", "forum", url_prefix="/api/forum", description="Forum API"
)
