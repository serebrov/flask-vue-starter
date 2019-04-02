import os


class Config:
    # Flask's general settings
    DEBUG = False

    # SQLAlchemy's general settings
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_MAX_OVERFLOW = 15
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI_ALEMBIC = os.getenv("SQLALCHEMY_DATABASE_URI_ALEMBIC")
    SQLALCHEMY_DATABASE_URI_CELERY = os.getenv("SQLALCHEMY_DATABASE_URI_CELERY")


class LocalConfig(Config):
    # Flask's general settings
    DEBUG = True
    JSONIFY_PRETTYPRINT_REGULAR = True

    SQLALCHEMY_DATABASE_URI = (
        os.getenv("SQLALCHEMY_DATABASE_URI") or "postgresql://localhost/forum"
    )  # noqa


config = {"local": LocalConfig}
