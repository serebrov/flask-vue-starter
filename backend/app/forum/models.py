from datetime import datetime

from app.extensions import db, Model
from app.user.models import User
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref


class Post(Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    text = db.Column(db.Text, nullable=False)

    created_by_user_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("user.id"), nullable=False
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.utcnow
    )

    user = db.relationship(User, backref=backref("posts", lazy="dynamic"))

    def __repr__(self):
        return "<Post %r>" % self.title


class Comment(Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True)
    post_id = db.Column(UUID(as_uuid=True), db.ForeignKey("post.id"), primary_key=True)
    text = db.Column(db.Text, nullable=False)

    created_by_user_id = db.Column(
        UUID(as_uuid=True), db.ForeignKey("user.id"), nullable=False
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.utcnow
    )

    def __repr__(self):
        return "<Comment %r>" % self.id
