from website.extensions import bcrypt, db
from website.models import User
from datetime import datetime


user1 = {
    "first-name": "Dwight",
    "last-name": "Frye",
    "email": "renfield@dracula.com",
    "dob": "1899-02-22",
    "tel": "9876543210",
    "password": "ratsratsrats",
    "confirm-password": "ratsratsrats"
}


user2 = {
    "first-name": "Bela",
    "last-name": "Lugosi",
    "email": "vlad3@dracula.com",
    "dob": "1882-10-20",
    "tel": "1234567890",
    "password": "iwanttosuckyourblood",
    "confirm-password": "iwanttosuckyourblood"
}


class TestSignup():
    def test_signup_page(self, client):
        response = client.get("/signup")
        assert response.status_code == 200


    def test_successful_signup(self, client, app):
        response = client.post("/signup", data=user1)
        assert response.status_code == 302
        with app.app_context():
            user = User.query.filter_by(email=user1["email"]).first()
            assert user is not None


    def test_new_user(self, app):
        new_user = User(
            first_name = user1["first-name"],
            last_name = user1["last-name"],
            email = user1["email"],
            dob = datetime.strptime(user1["dob"], "%Y-%m-%d").date(),
            tel = int(user1["tel"]),
            password = bcrypt.generate_password_hash(user1["password"]).decode('utf-8')
        )

        with app.app_context():
            db.session.add(new_user)
            db.session.commit()
            user = User.query.filter_by(email=user1["email"]).first()
            assert user is not None
            assert user.first_name == user1["first-name"]
            assert user.last_name == user1["last-name"]
            assert user.email == user1["email"]
            assert user.dob == datetime.strptime(user1["dob"], "%Y-%m-%d").date()
            assert user.tel == int(user1["tel"])
            assert bcrypt.check_password_hash(user.password, user1["password"])
            db.session.delete(user)
            db.session.commit()

    
    def test_invalid_first_name(self, client):
        user1_first_name = user1["first-name"]
        user1["first-name"] = ""
        response = client.post("/signup", data=user1)
        assert b'First name must be between 1 and 40 characters.' in response.data
        user1["first-name"] = user1_first_name


    def test_invalid_last_name(self, client):
        user1_last_name = user1["last-name"]
        user1["last-name"] = ""
        response = client.post("/signup", data=user1)
        assert b'Last name must be between 1 and 80 characters.' in response.data
        user1["last-name"] = user1_last_name


    def test_invalid_email(self, client):
        user1_email = user1["email"]
        user1["email"] = "renfield"
        response = client.post("/signup", data=user1)
        assert b'Invalid email address.' in response.data
        user1["email"] = user1_email

    
    def test_user_exists(self, client):
        client.post("/signup", data=user1)
        user2_email = user2["email"]
        user2["email"] = user1["email"]
        response = client.post("/signup", data=user2)
        assert b'That email already exists. Please choose a different one.' in response.data
        user2["email"] = user2_email

    
    def test_invalid_dob(self, client):
        user1_dob = user1["dob"]
        user1["dob"] = "18990222" 
        response = client.post("/signup", data=user1)
        assert b'Invalid date of birth format. Use YYYY-MM-DD.' in response.data
        user1["dob"] = user1_dob

    
    def test_invalid_password(self, client):
        user1_password = user1["password"]
        user1["password"] = "dracula"
        response = client.post("/signup", data=user1)
        assert b'Password must be between 8 and 20 characters.' in response.data
        user1["password"] = user1_password


    def test_invalid_confirm_password(self, client):
        user1_confirm_password = user1["confirm-password"]
        user1["confirm-password"] = "ratsratsratsrats"
        response = client.post("/signup", data=user1)
        assert b'Passwords must match.' in response.data
        user1["confirm-password"] = user1_confirm_password