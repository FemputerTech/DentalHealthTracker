"""
The application uses Flask to create a web interface and includes some modules:
- Index: Handles the main landing page

To run the application, execute this script.
"""
from website import create_app
from website.extensions import db


app = create_app()


# Create database tables if they don't exist
with app.app_context():
    db.create_all()


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)