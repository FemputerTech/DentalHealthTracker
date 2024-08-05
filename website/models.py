from .extensions import db
from flask_login import UserMixin
import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    tel = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    dentist_id = db.Column(db.Integer, nullable=True)

    chats = db.relationship('Chat', back_populates='user', cascade='all, delete-orphan')
    appointments = db.relationship('Appointment', back_populates='user')
    dental_records = db.relationship('DentalRecord', back_populates='user')


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(10), nullable=False)  # 'user' or 'bot'
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now())

    user = db.relationship('User', back_populates='chats')

class Dentist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False) 
    tel = db.Column(db.Integer, nullable=False)
    clinic_address = db.Column(db.String(255), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    license_number = db.Column(db.String(50), nullable=True)

    users = db.relationship('User', backref='dentist', lazy=True)