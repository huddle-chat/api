import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_TOKEN_LOCATION = 'cookies'
    JWT_ACCESS_COOKIE_NAME = 'access_token'
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET")
    JWT_CSRF_CHECK_FORM = True
    JWT_CSRF_IN_COOKIES = True
