"""
The application uses Flask to create a web interface and includes some modules:
- Index: Handles the main landing page

To run the application, execute this script.
"""
from website import create_app
from website.extensions import db, bcrypt
from website.models import User, Dentist
from datetime import datetime


app = create_app()

def seed_demo_user():
    if not User.query.first():
        demo_user = User(
            first_name="Hermione",
            last_name="Granger",
            email="hermione.granger@hogwarts.edu",
            dob = datetime.strptime("1979-09-19", "%Y-%m-%d").date(),
            tel = "5552221234",
            password = bcrypt.generate_password_hash("arithmancy179").decode('utf-8')
        )
        db.session.add(demo_user)
        db.session.commit()

def seed_dentists():
    if not Dentist.query.first():
        dentists = [
            Dentist(
                first_name="Vlad",
                last_name="Dracula",
                email="vlad.dracula@teeth.com",
                tel=5556667777,
                clinic_address="123 Transylvania Lane, Castle Dracul, Romania 54321",
                rating=4.9,
                license_number='D12345'
            ),
            Dentist(
                first_name="Freddy",
                last_name="Krueger",
                email="freddy.krueger@nightmare.com",
                tel=5551234567,
                clinic_address="1313 Elm Street, Suite 4, Springwood, OH 12345",
                rating=3.5,
                license_number='D23456'
            ),
            Dentist(
                first_name="Michael",
                last_name="Myers",
                email="michael.myers@halloween.com",
                tel=5559876543,
                clinic_address="40 Years Road, Haddonfield, IL 54321",
                rating=4,
                license_number='D34567'
            )
        ]

        db.session.bulk_save_objects(dentists)
        db.session.commit()


# Create database tables if they don't exist
with app.app_context():
    db.create_all()
    seed_demo_user()
    seed_dentists()


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)