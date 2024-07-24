"""
This module defines the view for logging into the Dental Health Tracker application.
"""
from flask import Blueprint, render_template
from flask.views import MethodView
from app.forms import LoginForm


login_blueprint = Blueprint('login', __name__)


class Login(MethodView):
    """
    Handles the login page.

    Methods:
    -------
    get(): Handles GET requests to the login page.
    post(): Handles POST requests to login.
    """
    
    def get(self):
        """
        Renders the login page.
        
        Returns:
        --------
        response : str
            The rendered HTML template for the login page.
        """
        form = LoginForm()
        return render_template('login.html', form=form)
    
    
    def post(self):
        """
        Renders the home page.
        
        Returns:
        --------
        response : str
            The rendered HTML template for the home page.
        """
        return render_template('index.html')


login_blueprint.add_url_rule('/login', view_func=Login.as_view('login'))