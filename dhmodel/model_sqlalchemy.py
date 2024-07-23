from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.string(120), unique=True, nullable=False)
    password = db.Column(db.string(80), nullable=False)