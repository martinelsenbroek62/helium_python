from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, String, Text, Boolean, Date, DateTime
from sqlalchemy.orm import relationship
from helium_flask.apps.config import db
from flask_login import UserMixin

from helium_flask.apps.helpers.models_helpers import BaseModel
# from helium_flask.apps.users.models import user_survey_association


class Survey(BaseModel):
    __tablename__ = 'surveys'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    created_by_id = Column(Integer, ForeignKey("survey.id"))
    create_by_rel = relationship("User",                                   back_populates="surveys_created")

    # attendees = relationship("User", secondary=user_survey_association, back_populates="surveys_attended")


class Questions(BaseModel):
    __tablename__ = 'surveys'

    id = Column(Integer, primary_key=True)
    statement = Column(String)

# class BenefitCategory(BaseModel):
#     uuid = Column(String)
#     name = Column(String)
#     focus_area = Column(String)
#     product_type = Column(String)
#     percent_to_reimburse = Column(String)
#     description = Column(Text)
#     focus_area_description = Column(Text)
#     product_type_description = Column(Text)
#     category_notes = Column(Text)
#     eligibility_description = Column(Text)
#     description_of_exclusions = Column(Text)
#     benefit_category_image_url = Column(Text)

    # organization_id = Column(Integer, ForeignKey("organizations.id"))
    # organization = relationship("Organization", back_populates="benefit_categories")


