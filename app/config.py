import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    UPLOAD_FOLDER = 'uploads'
    PROFILE_IMG_UPLOAD_FOLDER = os.path.join('uploads', 'profile_photos')
    CAR_IMG_UPLOAD_FOLDER = os.path.join('uploads', 'car_photos')
    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE_URL='postgres://gtzxwgnodjyuml:59a6d9357bb3c89245dd7e9238fc727e028e4a5a7dc73db34782b1c2ed416997@ec2-3-229-252-6.compute-1.amazonaws.com:5432/d8v5lsucjvfvhj'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed