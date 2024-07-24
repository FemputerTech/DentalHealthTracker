"""
The application uses Flask to create a web interface and includes some modules:
- Index: Handles the main landing page

To run the application, execute this script.
"""
from website import create_app


app = create_app()


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)