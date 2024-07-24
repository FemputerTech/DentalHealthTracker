from flask import Blueprint, render_template
from website.forms import SignupForm, LoginForm


auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    return render_template('signup.html', form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)