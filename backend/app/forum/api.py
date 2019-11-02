"""Forum API."""
from flask_rest_api import Blueprint, abort

blueprint = Blueprint(
    "forum", "forum", url_prefix="/api/forum", description="Forum API"
)
