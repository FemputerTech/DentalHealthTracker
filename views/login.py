"""
This module defines the view for logging into the Dental Health Tracker application.
"""
from flask import render_template
from flask.views import MethodView
from forms import LoginForm


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