import os
import pytest

from app.app import app
from app.extensions import db
from app.models.forum import User
from app.create_app import create_app


@pytest.fixture(scope='session')
def testapp():
    """A Flask test app."""
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_TEST_DATABASE_URI') or 'postgresql://testuser:testpw@postgresql:5432/forumtest'  # noqa
    return app


@pytest.fixture(scope='session')
def client(testapp):
    """A Flask test client. An instance of :class:`flask.testing.TestClient`
    by default.
    """
    return testapp.test_client()


@pytest.fixture(scope='session')
def _db(testapp):
    with testapp.app_context():
        db.create_all()
    return db


@pytest.fixture()
def user_factory(testapp, _db):
    """Return a function to create a ``User``."""
    def factory(username: str, email: str) -> User:
        with testapp.app_context():
            user = User(
                username=username,
                email=email,
            )
            db.session.add(user)
            db.session.commit()
            return user
    return factory


@pytest.fixture()
def user(user_factory):
    """Return a ``User``."""
    return user_factory(
        'test',
        'test@example.com',
    )
