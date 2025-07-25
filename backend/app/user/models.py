from uuid import uuid4

from app.extensions import db, Model
from sqlalchemy.dialects.postgresql import UUID


class User(Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, id=None, username=None, email=None):
        if not id:
            id = uuid4()
        self.id = id
        self.username = username
        self.email = email
        # Let SQLAlchemy handle the timestamps via column defaults

    def __repr__(self):
        return "<User %r>" % self.username
