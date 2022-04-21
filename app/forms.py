# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, PasswordField, BooleanField, FloatField, DateField, DateTimeField, SubmitField
from wtforms.validators import InputRequired



class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    name = StringField('Name', validators=[InputRequired()])
    location = StringField('Address', validators=[InputRequired()])
    biography = StringField('Biography', validators=[InputRequired()])      
    photo = FileField('Profile Picture', validators=[
        FileRequired(), 
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
#     register= SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Remember me')
#      login= SubmitField('Login')

class CarForm(FlaskForm):
    make = StringField('Make', validators=[InputRequired()])
    model = StringField('Model', validators=[InputRequired()])
    year = StringField('Year', validators=[InputRequired()])
    color = StringField('Color', validators=[InputRequired()])
    price = FloatField('Price', validators=[InputRequired()])
    image = FileField('Image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'gif'], 'Images only!')
    ])
    description = StringField('Description', validators=[InputRequired()])
    transmision = StringField('Transmision', validators=[InputRequired()])
    car_type = StringField('Car Type', validators=[InputRequired()])
