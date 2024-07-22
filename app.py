"""
The application uses Flask to create a web interface and includes some modules:
- Index: Handles the main landing page

To run the application, execute this script.
"""
from flask import Flask
from index import Index


app = Flask(__name__)


# URL routing for the main landing page
app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=['GET']
                 )


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)