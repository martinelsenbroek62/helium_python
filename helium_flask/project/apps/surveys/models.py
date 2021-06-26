# from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, JSON
# from sqlalchemy.orm import relationship
#
# from helium_flask.project.apps.helpers import BaseModel
# # from helium_flask.apps.users.models import user_survey_association
#
#
# class Survey(BaseModel):
#     __tablename__ = 'surveys'
#
#     name = Column(String)
#
#     created_by_id = Column(Integer, ForeignKey("survey.id"))
#     create_by_rel = relationship("User", back_populates="surveys_created")
#     is_master = Column(Boolean)
#     questions = relationship("Question")
#
#
#     attendees = relationship("User", secondary=user_survey_association, back_populates="surveys_attended")
#     def create():
#         if masterid:
#             master
#         else:
#             attendee
#
#
# class Question(BaseModel):
#     __tablename__ = 'surveys'
#
#     statement = Column(String)
#     options = Column(JSON)
#     answer = relationship("Answer")
#     category_id = Column()
#     category = relationship("Category", back_populates="questions")
#
# class Answer(BaseModel):
#     __tablename__ = 'answers'
#
#     answer = Column(String)
#     question_id = Column(Integer, ForeignKey("Question.id"))
#
# {   "survey": "",
#     "type": "",
#     "status": "in",
#     "questions": {
#         "page_1": [{"q_id": 1, "q_type": "text", "statment": "waht your name", "slected_vaue": ""},
#                    {"q_type": "checkbox", "values": ["value_1",.....]},
#                    ],
#         "page_last": [],
#
#     }}
# {"answers": {"questions": [{"q_id": 1, "slected_vaue": ""},....]}}
# class Category(BaseModel):
#     __tablename__ = "categories"
#
#     name = Column(String)
#     questions = relationship("Question", back_populates="category_id")

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


