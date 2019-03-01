from sqlalchemy.dialects.postgresql import UUID
from app import db


class User(db.Model):
    _id = Column(UUID(as_uuid=True), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):
    _id = Column(UUID(as_uuid=True), primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    text = db.Column(db.Text, False)

    _created_by_user_id = Column(
        UUID(as_uuid=True),
        db.ForeignKey('user.id'),
        nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False,
                        onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Post %r>' % self.title


class Comment(db.Model):
    _id = Column(UUID(as_uuid=True), primary_key=True)
    _post_id = Column(
        UUID(as_uuid=True),
        db.ForeignKey('post.id'),
        primary_key=True)
    text = db.Column(db.Text, False)

    _created_by_user_id = Column(
        UUID(as_uuid=True),
        db.ForeignKey('user.id'),
        nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False,
                        onupdate=datetime.utcnow)

    def __repr__(self):
        return '<Comment %r>' % self._id
