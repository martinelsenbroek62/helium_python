from sqlalchemy import Column, Integer, String
from flask_login import UserMixin

from helium_flask.project.helpers.generic_models import BaseModel


class BenefitCategoriesDemo(BaseModel):
    __tablename__ = "benefit_categories_demo"

    name = Column(String)
    focus_area = Column(String)

class User(UserMixin, BaseModel):
    __tablename__ = 'users'

    name = Column(String)
    email = Column(String)
    password = Column(String)
    password_hash = Column(String)
    password_salt = Column(String)
    abc = Column(String)


    def __repr__(self):
        return '<id {}>'.format(self.id)

