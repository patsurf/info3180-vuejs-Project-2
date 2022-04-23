# Add any model classes for Flask-SQLAlchemy here
from . import db
from werkzeug.security import generate_password_hash

class Cars(db.Model):
    __tablename__ = 'Cars' # set table name
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(length=255), nullable=False)
    make = db.Column(db.String(length=255), nullable=False)
    model = db.Column(db.String(length=180), nullable=False)
    color = db.Column(db.String(length=120), nullable=False)
    year = db.Column(db.String(length=120), nullable=False)
    transmission = db.Column(db.String(length=200), nullable=False)
    car_type = db.Column(db.String(length=80), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    image = db.Column(db.String(length=80), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    
    def __init__(self,description,make,model,color,year,transmission,car_type,price,image,user_id):
        self.description = description
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.car_type = car_type
        self.price = price
        self.image = image
        self.user_id = user_id

    def __repr__(self):
        return '<Cars %r>' % self.id
    
class Favourites(db.Model):
    __tablename__ = 'Favourites'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    car_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    
    def __init__(self,car_id,user_id):
        self.car_id = car_id
        self.user_id = user_id

    def __repr__(self):
        return '<Favourites %r>' % self.user_id
    
class Users(db.Model):
    __tablename__= 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=80), nullable=False)
    password = db.Column(db.String(length=255), nullable=False)
    name = db.Column(db.String(length=80), nullable=False)
    email = db.Column(db.String(length=80), nullable=False)
    location = db.Column(db.String(length=80), nullable=False)
    biography = db.Column(db.String(length=255), nullable=False)
    photo = db.Column(db.String(length=80), nullable=False)
    date_joined = db.Column(db.String(length=255), nullable=False)

    def __init__(self,username,password,name,email,location,biography,photo,date_joined):
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.name = name
        self.email = email
        self.location = location
        self.biography = biography
        self.photo = photo
        self.date_joined = date_joined
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
    
    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Users %r>' % self.username