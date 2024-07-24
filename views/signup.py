"""
This module defines the view for signing up for the Dental Health Tracker application.
"""
from flask import render_template, request, flash
from flask.views import MethodView
from forms import SignupForm


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