from flask import Flask
from flask_cors import CORS
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

import os


app = Flask(__name__, static_folder='../dist/assets')
app.config.from_object(Config)

# CSRF Protection
csrf = CSRFProtect(app)

# CORS
cors = CORS(app)

# Database
db = SQLAlchemy(app)

# Login manager
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'



# Migrate
migrate = Migrate(app, db)
from app import views
