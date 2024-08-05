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

    dentist_id = db.Column(db.Integer, db.ForeignKey('dentist.id'), nullable=True) # ForeignKey

    # Relationships
    chats = db.relationship('Chat', back_populates='user', cascade='all, delete-orphan')
    appointments = db.relationship('Appointment', back_populates='user')
    dental_records = db.relationship('DentalRecord', back_populates='user')


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # ForeignKey
    role = db.Column(db.String(10), nullable=False)  # 'user' or 'bot'
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now())

    # Relationship
    user = db.relationship('User', back_populates='chats')


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # ForeignKey
    appointment_date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    
    # Relationships
    user = db.relationship('User', back_populates='appointments')


class DentalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # ForeignKey
    record_date = db.Column(db.DateTime, nullable=False)
    dental_issue = db.Column(db.String(255), nullable=True)
    treatment_id = db.Column(db.Integer, db.ForeignKey('treatment.id'), nullable=True)
    
    # Relationships
    user = db.relationship('User', back_populates='dental_records')
    treatment = db.relationship('Treatment', backref='dental_records', lazy=True)



class Dentist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False) 
    tel = db.Column(db.Integer, nullable=False)
    clinic_address = db.Column(db.String(255), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    license_number = db.Column(db.String(50), nullable=True)

    # Relationship
    patients = db.relationship('User', backref='dentist', lazy=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Treatment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)