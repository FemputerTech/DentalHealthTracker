from website.extensions import bcrypt
from website.models import User
from datetime import datetime

class TestSignup():
    def test_successful_signup(self, client, app):
        response = client.post("/signup", data={
            "first-name": "Jane",
            "last-name": "Doe",
            "email": "test@test.com",
            "dob": "2024-01-01",
            "tel": "1234567890",
            "password": "testpassword",
            "confirm-password": "testpassword"
        })

        assert response.status_code == 200
        with app.app_context():
            assert User.query.count() == 2
            user = User.query.first()
            assert user.email == "test@test.com"
            assert bcrypt.check_password_hash(user.password, "testpassword")
