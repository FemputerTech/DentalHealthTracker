"""
This module defines the view for handling GET requests to the landing page
of the Dental Health Tracker application.
"""
from flask import render_template
from flask.views import MethodView


class Index(MethodView):
    """
    Handles the index page.

    Methods:
    -------
    get(): Handles GET requests to the index page.
    """
    
    
    def get(self):
        """
        Renders the index page.
        
        Returns:
        --------
        response : str
            The rendered HTML template for the index page.
        """
        print({"details":"It's aliiiiive!!"})
        return render_template('index.html')