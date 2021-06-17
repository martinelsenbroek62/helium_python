from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, String, Text, Boolean, Date, DateTime
from sqlalchemy.orm import relationship
from helium_flask.apps.config import db
from flask_login import UserMixin

from helium_flask.apps.helpers.models_helpers import BaseModel


class BenefitCategory(BaseModel):
    uuid = Column(String)
    name = Column(String)
    focus_area = Column(String)
    product_type = Column(String)
    percent_to_reimburse = Column(String)
    description = Column(Text)
    focus_area_description = Column(Text)
    product_type_description = Column(Text)
    category_notes = Column(Text)
    eligibility_description = Column(Text)
    description_of_exclusions = Column(Text)
    benefit_category_image_url = Column(Text)

    # organization_id = Column(Integer, ForeignKey("organizations.id"))
    # organization = relationship("Organization", back_populates="benefit_categories")


