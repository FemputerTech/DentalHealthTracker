from flask import Flask
from .extensions import db, bcrypt


def create_app(config_class='instance.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)

    from website.views.index import index_blueprint
    from website.views.auth import auth

    app.register_blueprint(index_blueprint)
    app.register_blueprint(auth)

    return app