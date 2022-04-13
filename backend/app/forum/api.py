"""Forum API."""
from flask_smorest import Blueprint

blueprint = Blueprint(
    "forum", "forum", url_prefix="/api/forum", description="Forum API"
)
