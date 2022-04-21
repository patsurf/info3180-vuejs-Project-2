"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, jsonify, send_file, send_from_directory, redirect
from flask_login import login_user, logout_user, current_user, login_required
import os
from app.models import Users, Cars, Favourites
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
from app.forms import LoginForm, CarForm, RegisterForm 

###
# Authentication
###

def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, app.config['SECRET_KEY'])
            user = Users.query.filter_by(email=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            # 401 is Unauthorized HTTP status code
            return jsonify(expired_msg), 401
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

# Login
@app.route('/api/auth/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/api/users/' + str(current_user.id))

    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = Users.query.filter_by(username=username).first()

            if user is not None and check_password_hash(user.password, password): 
                remember_me = False

            if 'remember_me' in request.form:
                remember_me = True
                login_user(user, remember=remember_me)
                return jsonify(message="Login successful", user=user.serialize(), redirect="/api/users/" + str(user.id))
            else:
                login_user(user)
                return jsonify(message="Login successful", user=user.serialize(), redirect="/api/users/" + str(user.id))
        else:
            return jsonify(message="Invalid username or password", errors=form_errors(form))

    return jsonify(message="Invalid request", user=None, redirect="/api/auth/login")

#check this
# @app.route('/api/auth/login', methods=['POST'])
# def login():
#     form = LoginForm()
#     if request.method == 'POST':
#         if form.validate_on_submit():
#             username = form.username.data
#             password = form.password.data
#             user = Users.query.filter_by(username=username).first()
#             if user is not None and check_password_hash(user.password, password):
#                     token = jwt.encode({'sub': user.username, 'iat': datetime.datetime.utcnow(), 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1440)}, app.config['SECRET_KEY'])
#                     response = {'token': token.decode('UTF-8')}
#                     return jsonify(response), 200
#             else:
#                 return jsonify(message="Incorrect username or password", authenticated=False), 401
#     return jsonify(message="Invalid request", authenticated=False), 400

# Register
@app.route('/api/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            name = form.name.data
            email = form.email.data
            location = form.location.data
            biography = form.biography.data
            photo = form.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            date_joined = form.date_joined.data
            user = Users(username,password,name,email,location,biography,filename,date_joined)
            db.session.add(user)
            db.session.commit()

            data = {
                username: username,
                password: password,
                name: name,
                email: email,
                location: location,
                biography: biography,
                photo: filename,
                date_joined: date_joined
            }
            return jsonify(message="Registration successful", user=data)
        else:
            return jsonify(message="Registration Unsuccessful", user=None, errors=form_errors(form))

    return jsonify(message="Invalid request", user=None)


# Car Form and List
@app.route('/api/cars', methods=['GET','POST'])
def cars():
    if request.method == 'GET':
        cars = Cars.query.all()
        return jsonify(cars=[car.serialize() for car in cars])
    elif request.method == 'POST':
        form = CarForm()
        if form.validate_on_submit():
            make = form.make.data
            model = form.model.data
            year = form.year.data
            color = form.color.data
            price = form.price.data
            image = form.image.data
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            description = form.description.data
            transmision = form.transmision.data
            car_type = form.car_type.data
            car = Cars(make,model,year,color,price,filename,description,transmision,car_type)
            db.session.add(car)
            db.session.commit()

            data = {
                make: make,
                model: model,
                year: year,
                color: color,
                price: price,
                image: filename,
                description: description,
                transmision: transmision,
                car_type: car_type
            }
            return jsonify(message="Car added successfully", car=data)
        else:
            return jsonify(message="Car not added successfully", car=None)

    return jsonify(message="Invalid request", car=None)

# Car Details
@app.route('/api/cars/<int:id>', methods=['GET'])
def car(id):
    if request.method == 'GET':
        car = Cars.query.get(id)
        return jsonify(car=car.serialize())

    return jsonify(message="Car not found", car=None)

# Favourites
@app.route('/api/cars/<int:id>/favourite', methods=['POST'])
@login_required
@token_required
def favourite(id):
    if request.method == 'POST':
        car = Cars.query.get(id)
        user = Users.query.get(1)
        favourite = Favourites(car,user)
        db.session.add(favourite)
        db.session.commit()
        return jsonify(message="Car added to favourites", car=car.serialize())

    return jsonify(message="Invalid request", car=None)

# Search
@app.route('/api/search', methods=['GET'])
def search():
    if request.method == 'GET':
        make = request.args.get('make')
        model = request.args.get('model')

        if make and model:
            cars = Cars.query.filter_by(make=make, model=model).all()
            return jsonify(cars=[car.serialize() for car in cars])
        elif make:
            cars = Cars.query.filter_by(make=make).all()
            return jsonify(cars=[car.serialize() for car in cars])
        elif model:
            cars = Cars.query.filter_by(model=model).all()
            return jsonify(cars=[car.serialize() for car in cars])
        else:
            cars = Cars.query.all()
            return jsonify(cars=[car.serialize() for car in cars])

    return jsonify(message="Invalid request", cars=None)

# User Details
@app.route('/api/users/<int:id>', methods=['GET'])
@token_required
@tlogin_required
def user(id):
    if request.method == 'GET':
        user = Users.query.get(id)
        return jsonify(user=user.serialize())

    return jsonify(message="Invalid request", user=None)

# User Favourites
@app.route('/api/users/<int:id>/favourites', methods=['GET'])
@token_required
@login_required
def favourites(id):
    if request.method == 'GET':
        user = Users.query.get(id)
        favourites = Favourites.query.filter_by(user=user).all()
        return jsonify(favourites=[favourite.serialize() for favourite in favourites])

    return jsonify(message="Invalid request", favourites=None)

# Logout
@app.route('/api/logout', methods=['GET','POST'])
def logout():
    return jsonify(message="Logout successful")

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
