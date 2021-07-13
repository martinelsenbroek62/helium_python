from os import getenv
from flask_sqlalchemy import SQLAlchemy


def configure_app(app):
    app.config['CORS_HEADERS'] = 'Content-Type'
    # app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///helium"
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/helium_flask"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "secret"

    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    # test account creds
    app.config['MAIL_USERNAME'] = "oldnightsproject@gmail.com"
    app.config['MAIL_PASSWORD'] = "oldnights123"
    # app.config["MAIL_USERNAME"] = getenv("MAIL_USERNAME")
    # app.config["MAIL_PASSWORD"] = getenv("MAIL_PASSWORD")
    app.config["MAIL_USE_TLS"] = False
    app.config["MAIL_USE_SSL"] = True
    app.config['JWT_ACCESS_LIFESPAN'] = {'hours': 24}
    app.config['JWT_REFRESH_LIFESPAN'] = {'days': 30}
    return app


def initialize_db(app):
    return SQLAlchemy(app=app)
