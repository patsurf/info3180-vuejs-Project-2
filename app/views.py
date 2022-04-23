"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from datetime import datetime, timedelta
from app import app, db
from flask import render_template, request, jsonify, g, send_from_directory, session, _request_ctx_stack
from flask_login import login_user, logout_user, current_user, login_required
import os
from app.models import Users, Cars, Favourites
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import LoginForm, CarForm, RegisterForm, SearchCars
import jwt
from functools import wraps
from flask_wtf.csrf import generate_csrf



###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")



#Login
@app.route('/api/auth/login', methods=['POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = Users.query.filter_by(username=username).first()
            if user is not None and check_password_hash(user.password, password):
                    payload = {'id': user.id, 'username': user.username}
                    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
                    auth = True
                    response = {'token': token, 'message':"User Logged In", 'auth': auth, 'user_id': user.id}
                    return jsonify(response), 200
            else:
                auth = False
                token = ''
                payload = {'id': '', 'username': ''}
                response = {'token': token, 'errmessage':"Invalid Credentials", 'auth': auth}
                return jsonify(response), 401
    return jsonify(response), 401



#Register
@app.route('/api/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        form.username.data = request.form['username']
        form.password.data = request.form['password']
        form.email.data = request.form['email']
        form.name.data = request.form['name']
        form.location.data = request.form['location']
        form.biography.data = request.form['biography']
        form.photo.data = request.files['photo']
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            name = form.name.data
            email = form.email.data
            location = form.location.data
            biography = form.biography.data
            photo = form.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['PROFILE_IMG_UPLOAD_FOLDER'], filename))
            date_joined = format_date_joined(datetime.now())
            user = Users(username,password,name,email,location,biography,filename,date_joined)
            db.session.add(user)
            db.session.commit()

            return jsonify(message = "Registration successful" , errors=form_errors(form))
        else:
            return jsonify(errmessage="Registration Unsuccessful", user=None, errors=form_errors(form))



# Car Form and List
@app.route('/api/cars', methods=['GET','POST'])
def cars():
    form = CarForm()
    if request.method == 'GET':
        cars = Cars.query.order_by(Cars.id).all()
        allCars = []
        message = "Here are all the cars"
        for car in cars:
            car_dict = {
                'id': car.id,
                'make': car.make,
                'model': car.model,
                'year': car.year,
                'price': car.price,
                'image': car.image,
                'description': car.description,
                'user_id': car.user_id,
                'color': car.color,
                'transmission': car.transmission,
                'car_type': car.car_type
            }
            allCars.append(car_dict)
        return jsonify(allCars = allCars, message = message)
        
    elif request.method == 'POST':
        form.description.data = request.form['description']
        form.make.data = request.form['make']
        form.model.data = request.form['model']
        form.year.data = request.form['year']
        form.color.data = request.form['color']
        form.price.data = request.form['price']
        form.image.data = request.files['image']
        form.car_type.data = request.form['car_type']
        form.transmission.data = request.form['transmission']
        form.user_id.data = request.form.get('user_id', type=int)
        if form.validate_on_submit():
            make = form.make.data
            model = form.model.data
            year = form.year.data
            color = form.color.data
            price = form.price.data
            image = form.image.data
            description = form.description.data
            transmission = form.transmission.data
            car_type = form.car_type.data
            user_id = form.user_id.data
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['CAR_IMG_UPLOAD_FOLDER'], filename))
            car = Cars(description,make,model,color,year,transmission,car_type,price,filename,user_id)
            db.session.add(car)
            db.session.commit()
            return jsonify(message="Car added successfully", errors=form_errors(form))
        else:
            return jsonify(message="Car not added successfully", car=None, errors=form_errors(form))

    return jsonify(message="Invalid request", car=None)

# Car Details
@app.route('/api/cars/<int:id>', methods=['GET'])
def car(id):
    if request.method == 'GET':
        car = Cars.query.get(id)
        if car:
            message = "Here is the car you requested"
            make = car.make
            model = car.model
            year = car.year
            price = car.price
            image = car.image
            description = car.description
            transmission = car.transmission
            car_type = car.car_type
            user_id = car.user_id
            color = car.color
            return jsonify(message=message, make=make, model=model, year=year, price=price, image=image, description=description, transmission=transmission, car_type=car_type, user_id=user_id, color=color),200

    return jsonify(message="Car not found", car=None)

# Favourite
@app.route('/api/cars/<int:id>/favourite', methods=['POST'])
# @login_required
# @token_required
def favourite(id):
    if request.method == 'POST':
        user_id = request.form['user_id']
        favourite = Favourites(id,user_id)
        db.session.add(favourite)
        db.session.commit()
        return jsonify(message="Car added to favourites")

    return jsonify(message="Invalid request", car=None)

# Search
@app.route('/api/search', methods=['GET','POST'])
def search():
    form = SearchCars()
    if request.method == 'POST':
        make = form.make.data
        model = form.model.data
        if make and model:
            cars = Cars.query.filter_by(make=make, model=model).all()
            allCars = []
            message = "Here are all the cars"
            for car in cars:
                car_dict = {
                    'id': car.id,
                    'make': car.make,
                    'model': car.model,
                    'year': car.year,
                    'price': car.price,
                    'image': car.image,
                    'description': car.description,
                    'user_id': car.user_id,
                    'color': car.color,
                    'transmission': car.transmission,
                    'car_type': car.car_type
                }
                allCars.append(car_dict)
            return jsonify(allCars = allCars, message = message)
        elif make:
            cars = Cars.query.filter_by(make=make).all()
            allCars = []
            message = "Here are all the cars"
            for car in cars:
                car_dict = {
                    'id': car.id,
                    'make': car.make,
                    'model': car.model,
                    'year': car.year,
                    'price': car.price,
                    'image': car.image,
                    'description': car.description,
                    'user_id': car.user_id,
                    'color': car.color,
                    'transmission': car.transmission,
                    'car_type': car.car_type
                }
                allCars.append(car_dict)
            return jsonify(allCars = allCars, message = message)
        elif model:
            cars = Cars.query.filter_by(model=model).all()
            allCars = []
            message = "Here are all the cars"
            for car in cars:
                car_dict = {
                    'id': car.id,
                    'make': car.make,
                    'model': car.model,
                    'year': car.year,
                    'price': car.price,
                    'image': car.image,
                    'description': car.description,
                    'user_id': car.user_id,
                    'color': car.color,
                    'transmission': car.transmission,
                    'car_type': car.car_type
                }
                allCars.append(car_dict)
            return jsonify(allCars = allCars, message = message)
        else:
            cars = Cars.query.all()
            allCars = []
            message = "Here are all the cars"
            for car in cars:
                car_dict = {
                    'id': car.id,
                    'make': car.make,
                    'model': car.model,
                    'year': car.year,
                    'price': car.price,
                    'image': car.image,
                    'description': car.description,
                    'user_id': car.user_id,
                    'color': car.color,
                    'transmission': car.transmission,
                    'car_type': car.car_type
                }
                allCars.append(car_dict)
            return jsonify(allCars = allCars, message = message)
    return jsonify(message="Invalid request", cars=None, errors=form_errors(form))

# User Details
@app.route('/api/users/<int:id>', methods=['GET'])
# @token_required
# @login_required
def user(id):
    if request.method == 'GET':
        user = Users.query.filter_by(id=id).first()
        user_id = user.id
        name = user.name
        username = user.username
        email = user.email
        location = user.location
        biography = user.biography
        date_joined = user.date_joined
        profile_img = user.photo
        message = "Sucessfully found profile"
        return jsonify(user_id = user_id, name=name, username=username, email=email, location=location, biography=biography, date_joined=date_joined, profile_img=profile_img, message=message)

    return jsonify(message="Error", user=None)

# User Favourites
@app.route('/api/users/<int:id>/favourites', methods=['GET'])
# @token_required
# @login_required
def favourites(id):
    if request.method == 'GET':
        user = Users.query.filter_by(id=id).first()
        user_id = user.id
        favMessage = "Sucessfully found profile"
        favourites = Favourites.query.filter_by(user_id=id).all()
        allFavourites = []
        for favourite in favourites:
            car = Cars.query.filter_by(id=favourite.car_id).first()
            car_dict = {
                'id': car.id,
                'make': car.make,
                'model': car.model,
                'year': car.year,
                'price': car.price,
                'image': car.image,
                'description': car.description,
                'user_id': car.user_id,
                'color': car.color,
                'transmission': car.transmission,
                'car_type': car.car_type
            }
            allFavourites.append(car_dict)
        return jsonify(allFavourites=allFavourites, favMessage=favMessage),200

    return jsonify(message="Invalid request", favourites=None)

# Date Joined Editor
def format_date_joined(date):
    return "Joined " + date.strftime("%B %d, %Y")

# Logout
@app.route('/api/logout', methods=['GET','POST'])
def logout():
    return jsonify(message="Logout successful")

# Generate CSRF Token
@app.route('/api/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

# Get Profile images
# def get_profile_image(filename):
#     return send_from_directory(os.path.join(os.getcwd(),app.config['PROFILE_IMG_UPLOAD_FOLDER']), filename)

# #Get Car Images
# def get_car_image(filename):
#     return send_from_directory(os.path.join(os.getcwd(),app.config['CAR_IMG_UPLOAD_FOLDER']), filename)


###
# Authentication
###

# def token_required(f):
#   @wraps(f)
#   def decorated(*args, **kwargs):
#     token = None

#     if 'Authorization' in request.headers:
#       token = request.headers['Authorization']

#     if not token:
#       return jsonify({'message' : 'Token is missing!'}), 401

#     try:
#       data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
#       current_user = Users.query.filter_by(id=data['user.id']).first()
#     except:
#       return jsonify({'message' : 'Token is invalid!'}), 401

#     return f(current_user, *args, **kwargs)

#   return decorated

# @app.route('/api/secure', methods=['GET'])
# @token_required
# def api_secure():
#     user = g.current_user
#     return jsonify(data={"user": user}, message="Success")

###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
