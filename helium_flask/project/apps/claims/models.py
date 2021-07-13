from sqlalchemy import String, Column, Text, Integer, Boolean, Date
from helium_flask.project.apps import db

from helium_flask.project.helpers.generic_models import BaseModel


# class BenefitCategories(BaseModel):
#     __tablename__ = "benefit_categories"
#
#     name = Column(String)
#     focus_area = Column(String)
#     product_type = Column(String)
#     percent_to_reimburse = Column(String)
#     description = Column(Text)
#     focus_area_description = Column(Text)
#     product_type_description = Column(Text)
#
#
# class BenefitPrograms(BaseModel):
#     __tablename__ = "benefit_programs"
#
#     name = Column(String)
#     description = Column(Text)
#     program_notes = Column(Text)
#
#
# class Claims(BaseModel):
#     __tablename__ = "claims"
#
#     title = Column(String)
#     description = Column(Text)
#     purchase_amount = Column(Integer)
#     reimbursement_amount = Column(Integer)
#
#     requesting_reason = Column(String)
#     requesting_amount = Column(Integer)
#
#     approved = Column(Boolean)
#     rejected = Column(Boolean)
#     paid_out = Column(Boolean)
#
#     rejected_reason = Column(String)
#
# class Funds(BaseModel):
#     __tablename__ = "funds"
#
#     amount = Column(Boolean)
#     comment = Column(String)
#     available_on = Column(Date)
