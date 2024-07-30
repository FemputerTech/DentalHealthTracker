"""
Setting up test environment
"""
import pytest
from website import create_app
from website.extensions import db, bcrypt
from website.models import User
from datetime import datetime


user1 = {
    "first-name": "Dwight",
    "last-name": "Frye",
    "email": "renfield@dracula.com",
    "dob": "1899-02-22",
    "tel": "9876543210",
    "password": "ratsratsrats",
    "confirm-password": "ratsratsrats"
}


user2 = {
    "first-name": "Bela",
    "last-name": "Lugosi",
    "email": "vlad3@dracula.com",
    "dob": "1882-10-20",
    "tel": "1234567890",
    "password": "iwanttosuckyourblood",
    "confirm-password": "iwanttosuckyourblood"
}



@pytest.fixture()
def app():
    app = create_app('instance.config.TestConfig')

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()