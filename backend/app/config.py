import os


class Config:
    # Flask's general settings
    DEBUG = False

    # SQLAlchemy's general settings
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 5,
        'max_overflow': 15
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI_ALEMBIC = os.getenv("SQLALCHEMY_DATABASE_URI_ALEMBIC")
    SQLALCHEMY_DATABASE_URI_CELERY = os.getenv("SQLALCHEMY_DATABASE_URI_CELERY")

    # flask-smorest
    API_TITLE = "Flask Vue Starter API"
    API_VERSION = "0.1"
    OPENAPI_VERSION = "3.0.2"


class LocalConfig(Config):
    # Flask's general settings
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = (
        os.getenv("SQLALCHEMY_DATABASE_URI") or "postgresql://localhost/forum"
    )  # noqa


class TestingConfig(Config):
    """Unit testing settings."""

    DEBUG = True
    EXPLAIN_TEMPLATE_LOADING = False
    SQLALCHEMY_DATABASE_URI = (
        os.getenv("SQLALCHEMY_TEST_DATABASE_URI") or "sqlite:///:memory:"
    )


class DevelopConfig(Config):
    """Develop environment settings."""

    DEBUG = os.environ.get("DEBUG", "False") == "True"


class ProductionConfig(Config):
    """Production environment settings."""

    DEBUG = os.environ.get("DEBUG", "False") == "True"


config = {
    "local": LocalConfig,
    "testing": TestingConfig,
    "develop": DevelopConfig,
    "production": ProductionConfig,
}
