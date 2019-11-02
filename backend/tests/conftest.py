import os
import pytest

from sqlalchemy import create_engine
import sqlalchemy as sa

from app.core.create_app import create_app
from app.extensions import db
from app.user.models import User


# Retrieve a database connection string from the shell environment
try:
    DB_CONN = os.environ["SQLALCHEMY_TEST_DATABASE_URI"]
except KeyError:
    raise KeyError(
        "SQLALCHEMY_TEST_DATABASE_URI not found. "
        + "You must export a database "
        + "connection string to the environmental variable "
        + "SQLALCHEMY_TEST_DATABASE_URI in order to run tests."
    )
else:
    DB_OPTS = sa.engine.url.make_url(DB_CONN).translate_connect_args()


@pytest.fixture(scope="session")
def database(request):
    """
    Drop and create a Postgres database for the tests.
    """

    pg_db = DB_OPTS["database"]
    # We will connect to 'template1' DB to be able to drop / create the test DB.
    standard_db = "postgresql://{username}:{password}@{host}:5432/template1".format(
        **DB_OPTS
    )

    if "test" not in pg_db:
        raise Exception(
            "Is this correct db {}? "
            "We assume the test db should "
            "have word `test` in its name.".format(pg_db)
        )

    engine = create_engine(standard_db)
    connection = engine.connect()
    connection.execute("commit")
    connection.execute("drop database if exists {}".format(pg_db))
    connection.execute("commit")
    connection.execute("create database {}".format(pg_db))
    connection.close()


@pytest.fixture(scope="session")
def app(database):
    """A Flask test app."""
    flask_app = create_app("testing")
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = DB_CONN
    with flask_app.app_context():
        yield flask_app


@pytest.fixture(scope="session")
def client(app):
    """A Flask test client. An instance of :class:`flask.testing.TestClient`
    by default.
    """
    return app.test_client()


@pytest.fixture(scope="session")
def _db(app):
    """Special fixture for pytest-flask-sqlalchemy.

    The pytest-flask-sqlalchemy provides `db_session` to be used in
    tests.
    That fixture automatically handles transactions - the data created
    during the test, will be removed from the database after the test.
    """
    db.create_all()
    return db


@pytest.fixture()
def user_factory(app, db_session):
    """Return a function to create a ``User``."""

    def factory(username: str, email: str) -> User:
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    return factory


@pytest.fixture()
def user(user_factory):
    """Return a ``User``."""
    return user_factory("test", "test@example.com")
