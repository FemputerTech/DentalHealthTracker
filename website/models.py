"""
User -> Chat (one-to-many) For every one user we can have many chats (ForeignKey: chat.user_id)
User -> Appointment (one-to-many) For every one user we can have many appointments (ForeignKey: appointment.user_id)
User -> DentalRecord (one-to-many) For every one user we can have many dental records (ForeignKey: dental_record.user_id)

Dentist -> User (one-to-many) For every one dentist we can have many users (patients) (ForeignKey: user.dentist_id)
Dentist -> Appointment (one-to-many) For every one dentist we can have many appointments (ForeignKey: appointment.dentist_id)
"""
from .extensions import db
from flask_login import UserMixin
import datetime


class User(db.Model, UserMixin):
    """
    Represents a user in the system.
    
    Attributes:
        id: Integer, primary key.
        dentist_id: Integer, foreign key referencing Dentist.
        first_name: String, user's first name.
        last_name: String, user's last name.
        email: String, user's email, unique.
        dob: Date, user's date of birth.
        tel: String, user's telephone number.
        password: String, user's hashed password.
        chats: Relationship to Chat, one-to-many.
        appointments: Relationship to Appointment, one-to-many.
        dental_records: Relationship to DentalRecord, one-to-many.
    """
    id = db.Column(db.Integer, primary_key=True)
    dentist_id = db.Column(db.Integer, db.ForeignKey('dentist.id'), nullable=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    tel = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    chats = db.relationship('Chat', backref='user') # Relationship
    appointments = db.relationship('Appointment', backref='user') # Relationship
    dental_records = db.relationship('DentalRecord', backref='user') # Relationship


class Dentist(db.Model):
    """
    Represents a dentist in the system.
    
    Attributes:
        id: Integer, primary key.
        first_name: String, dentist's first name.
        last_name: String, dentist's last name.
        email: String, dentist's email, unique.
        tel: String, dentist's telephone number.
        clinic_address: String, address of the clinic.
        rating: Float, rating of the dentist.
        license_number: String, dentist's license number.
        patients: Relationship to User, one-to-many.
        appointments: Relationship to Appointment, one-to-many.
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False) 
    tel = db.Column(db.Integer, nullable=False)
    clinic_address = db.Column(db.String(255), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    license_number = db.Column(db.String(50), nullable=True)

    patients = db.relationship('User', backref='dentist') # Relationship
    appointments = db.relationship('Appointment', backref='dentist') # Relationship

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    

class Chat(db.Model):
    """
    Represents a chat message between a user and the bot.
    
    Attributes:
        id: Integer, primary key.
        user_id: Integer, foreign key referencing User.
        role: String, role of the sender ('user' or 'bot').
        content: Text, message content.
        timestamp: DateTime, time the message was sent.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now())


class Appointment(db.Model):
    """
    Represents an appointment scheduled by a user.
    
    Attributes:
        id: Integer, primary key.
        user_id: Integer, foreign key referencing User.
        dentist_id: Integer, foreign key referencing Dentist.
        service_id: Integer, foreign key referencing Service.
        appointment_date: DateTime, date and time of the appointment.
        notes: Text, additional notes for the appointment.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    dentist_id = db.Column(db.Integer, db.ForeignKey('dentist.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    appointment_date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.Text, nullable=True)


class DentalRecord(db.Model):
    """
    Represents a user's dental record.
    
    Attributes:
        id: Integer, primary key.
        user_id: Integer, foreign key referencing User.
        service_id: Integer, foreign key referencing Service.
        record_date: DateTime, date of the dental record.
        dental_issue: String, description of the dental issue.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    record_date = db.Column(db.DateTime, nullable=False)
    dental_issue = db.Column(db.String(255), nullable=True)


class Services(db.Model):
    """
    Represents a dental services.
    
    Attributes:
        id: Integer, primary key.
        name: String, name of the service.
        description: Text, description of the service.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)