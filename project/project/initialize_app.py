from flask import Flask

from os import getenv

from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


def configure_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///helium"
    # app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "secret"

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = getenv("MAIL_USERNAME")
    app.config['MAIL_PASSWORD'] = getenv("MAIL_PASSWORD")
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    return app

def initialize_db(app):
    return SQLAlchemy(app=app)

def initialize_login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    return login_manager

app = Flask(__name__, static_folder="../static", template_folder="../templates")
app = configure_app(app)
db = initialize_db(app)
login_manager = initialize_login_manager(app)