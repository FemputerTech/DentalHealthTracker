"""
This module defines the view for handling GET requests to the home page
of the Dental Health Tracker application.
"""
from flask import render_template
from flask.views import MethodView


class Index(MethodView):
    """
    Handles the index (home) page.

    Methods:
    -------
    get(): Handles GET requests to the index (home) page.
    """
    
    
    def get(self):
        """
        Renders the index (home) page.
        
        Returns:
        --------
        response : str
            The rendered HTML template for the index page.
        """
        return {"details":"It's aliiiiive!!"}