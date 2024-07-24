from flask import Flask
from .extensions import db, bcrypt


def create_app(config_class='instance.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)

    from website.views import views
    from website.auth import auth

    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app