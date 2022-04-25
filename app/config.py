import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    UPLOAD_FOLDER = 'uploads'
    PROFILE_IMG_UPLOAD_FOLDER = 'uploads\profile_photos'
    CAR_IMG_UPLOAD_FOLDER = 'uploads\car_photos'
    SECRET_KEY = 'r@ndomK3y'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed'
    