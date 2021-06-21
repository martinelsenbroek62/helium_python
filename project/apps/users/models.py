from sqlalchemy import Column, Integer, String
from flask_login import UserMixin

from helium_flask.project.helpers.models import BaseModel

# user_survey_association = Table("user_survey_association",
#                                 user_id = Column(Integer, ForeignKey("users.id"), primary_key=True),
#                                 survey_id = Column(Integer, ForeignKey("survey.id"), primary_key=True))


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
    # surveys_attended = relationship("Survey",
    #                                 seconday=user_survey_association, back_populates="attendees")
    # surveys_created = relationship("Survey",
    #                                back_populates="created_by")


    # uuid = Column(String)
    # username = Column(String)
    # first_name = Column(String)
    # last_name = Column(String)
    # employee_office_location = Column(String)
    # employee_state_of_residence = Column(String)
    # employee_invite_uuid = Column(String)
    # saml_idp = Column(String)
    #
    # super_admin = Column(Boolean)
    # organization_admin = Column(Boolean)
    #
    # employee_start_date = Column(Date)
    # employee_termination_date = Column(Date)


    def __repr__(self):
        return '<id {}>'.format(self.id)


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
#
#     # organization_id = Column(Integer, ForeignKey("organizations.id"))
#     # organization = relationship("Organization", back_populates="benefit_categories")
#
#