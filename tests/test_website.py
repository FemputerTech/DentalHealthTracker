from website.models import User
from website.extensions import db


def test_app_creation(app):
    """Test if the application is created correctly."""
    assert app is not None
    assert app.config['TESTING'] is True
    assert app.config['SECRET_KEY'] is not None


def test_blueprints_registered(app):
    """Test if the expected blueprints are registered with the application."""
    assert 'auth' in app.blueprints
    assert 'views' in app.blueprints
    assert 'dash' in app.blueprints
    assert 'bot' in app.blueprints