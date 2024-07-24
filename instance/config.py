import os

class Config:
    BASE_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = 'my-secure-secret-key'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIRECTORY, '../website/database.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
