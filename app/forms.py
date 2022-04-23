# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, BooleanField, FloatField, DateField, DateTimeField, IntegerField
from wtforms.validators import InputRequired, DataRequired



class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    name = StringField('Name', validators=[InputRequired()])
    location = StringField('Address', validators=[InputRequired()])
    biography = StringField('Biography', validators=[InputRequired()])      
    photo = FileField('Profile Picture', validators=[
        FileRequired(), 
        FileAllowed(['jpeg','jpg', 'png'], 'Images only!')
    ])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Remember me')

class CarForm(FlaskForm):
    make = StringField('Make', validators=[InputRequired()])
    model = StringField('Model', validators=[InputRequired()])
    year = StringField('Year', validators=[InputRequired()])
    color = StringField('Color', validators=[InputRequired()])
    price = FloatField('Price', validators=[InputRequired()])
    image = FileField('Image', validators=[
        FileRequired(),
        FileAllowed(['jpeg','jpg', 'png', 'gif'], 'Images only!')
    ])
    description = StringField('Description', validators=[InputRequired()])
    transmission = StringField('Transmision', validators=[InputRequired()])
    car_type = StringField('Car Type', validators=[InputRequired()])
    user_id = StringField('User ID', validators=[InputRequired()])

class SearchCars(FlaskForm):
    make = StringField('Make', validators=[InputRequired()])
    model = StringField('Model', validators=[InputRequired()])