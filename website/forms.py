from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.widgets import TelInput
from website.models import User


class SignupForm(FlaskForm):
    first_name = StringField(
        validators=[DataRequired(), Length(min=1, max=40)],
        render_kw={"placeholder": "First name"}
    )
    last_name = StringField(
        validators=[DataRequired(), Length(min=1, max=80)],
        render_kw={"placeholder": "Last name"}
    )
    email = StringField(
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Email"}
    )
    dob = DateField(
        validators=[DataRequired()],
        format='%Y-%m-%d'
    )
    tel = StringField(
        validators=[DataRequired()],
        widget=TelInput(),
        render_kw={"placeholder": "123-456-7890"}
    ) 
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=8, max=20)],
        render_kw={"placeholder": "Password"}
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")],
        render_kw={"placeholder": "Confirm password"}
    )
    submit = SubmitField("Sign Up")

    def validate_email(self, email):
        existing_user = User.query.filter_by(email=email.data).first()
        
        if existing_user:
            raise ValidationError("That email already exists. Please choose a different one.")
        

class LoginForm(FlaskForm):
    email = StringField(
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Email"}
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=8, max=20)],
        render_kw={"placeholder": "Password"}
    )
    submit = SubmitField("Login")
