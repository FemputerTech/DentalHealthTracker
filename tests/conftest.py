"""
Setting up test environment
"""
import pytest
from website import create_app
from website.extensions import db

@pytest.fixture()
def app():
    app = create_app('instance.config.TestConfig')

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    yield app


@pytest.fixture
def client(app):
    return app.test_client()
