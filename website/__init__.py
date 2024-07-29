from flask import Flask
from .extensions import db, bcrypt, login_manager
from .models import User


def create_app(config_class='instance.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from website.auth import auth
    from website.views import views
    from website.dashboard import dash
    from website.openai import bot

    app.register_blueprint(auth)
    app.register_blueprint(views)
    app.register_blueprint(dash)
    app.register_blueprint(bot)

    return app