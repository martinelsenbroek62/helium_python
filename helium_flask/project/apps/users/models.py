import uuid

from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash

from helium_flask.project.project.initialize_app import app, guard
from helium_flask.project.helpers.generic_models import BaseModel
from helium_flask.project.project.initialize_app import db
from helium_flask.project.apps.surveys.models import SurveyUser



class User(BaseModel):
    __tablename__ = "users"

    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    survey_user = db.relationship("SurveyUser", back_populates="user", uselist=False)
    roles = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True, server_default="true")

    def __repr__(self):
        return "<id {}>".format(self.id)

    # _password = db.Column(db.String)
    #
    # @hybrid_property
    # def password(self):
    #     return self._password
    #
    # @password.setter
    # def password(self, password):
    #     self._password = generate_password_hash(password, method="sha256")


    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, email):
        return cls.query.filter_by(email=email).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    def is_valid(self):
        return self.is_active

class Token(BaseModel):
    __tablename__ = "tokens"

    token_string = db.Column(db.String, default=uuid.uuid4())
    email = db.Column(db.String)


with app.app_context():
    guard.init_app(app, User)
