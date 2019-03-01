from datetime import datetime
from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref, relationship
from sqlalchemy.schema import Column

from app.extensions import db


class User(db.Model):
    id = Column(UUID(as_uuid=True), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, id=None, username=None, email=None):
        if not id:
            id = uuid4()
        self.id = id
        self.created_at = datetime.utcnow()
        self.last_modified_at = self.created_at
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    id = Column(UUID(as_uuid=True), primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    text = db.Column(db.Text, nullable=False)

    created_by_user_id = Column(
        UUID(as_uuid=True),
        db.ForeignKey('user.id'),
        nullable=False)
    created_at = Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(db.DateTime, default=datetime.utcnow, nullable=False,
                        onupdate=datetime.utcnow)


    user = relationship(
        'User',
        backref=backref('posts', lazy='dynamic')
    )

    def __repr__(self):
        return '<Post %r>' % self.title


class Comment(db.Model):
    id = Column(UUID(as_uuid=True), primary_key=True)
    post_id = Column(
        UUID(as_uuid=True),
        db.ForeignKey('post.id'),
        primary_key=True)
    text = db.Column(db.Text, nullable=False)

    created_by_user_id = Column(
        UUID(as_uuid=True),
        db.ForeignKey('user.id'),
        nullable=False)
    created_at = Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(db.DateTime, default=datetime.utcnow, nullable=False,
                        onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Comment %r>' % self.id
