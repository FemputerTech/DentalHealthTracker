"""
This module defines the view for signing up for the Dental Health Tracker application.
"""
from flask import Blueprint, render_template
from flask.views import MethodView
from website.forms import SignupForm


signup_blueprint = Blueprint('signup', __name__)


class Signup(MethodView):
    """
    Handles the signup page.

    Methods:
    -------
    get(): Handles GET requests to the signup page.
    post(): Handles POST requests to signup.
    """
    
    def get(self):
        """
        Renders the signup page.
        
        Returns:
        --------
        response : str
            The rendered HTML template for the signup page.
        """
        form = SignupForm()
        return render_template('signup.html', form=form)
    
    
    def post(self):
        """
        Renders the home page.
        
        Returns:
        --------
        response : str
            The rendered HTML template for the home page.
        """        
        return render_template('index.html')


signup_blueprint.add_url_rule('/signup', view_func=Signup.as_view('signup'))