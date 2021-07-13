from helium_flask.project.helpers.generic_models import BaseModel

from helium_flask.project.project.initialize_app import db


class Organization(BaseModel):
    __tablename__ = "organizations"

    name = db.Column(db.String)
    surveys = db.relationship("Survey", back_populates="organization")
    pass_code = db.Column(db.String)


class Survey(BaseModel):
    __tablename__ = "surveys"

    name = db.Column(db.String)
    slug = db.Column(db.String, unique=True)

    created_by_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # is_active = db.Column(db.Boolean)
    categories = db.relationship("Category", back_populates="survey")
    survey_users = db.relationship("SurveyUser", back_populates="survey")

    organization_id = db.Column(db.Integer, db.ForeignKey("organizations.id"))
    organization = db.relationship("Organization", back_populates="surveys")

    # def get_survey_questions(self):
    #     Group.filter(Group.category_id.in_([s.id for s in self.categories]))


class SurveyUser(BaseModel):
    __tablename__ = "survey_users"

    survey_id = db.Column(db.Integer, db.ForeignKey("surveys.id"))
    survey = db.relationship("Survey", back_populates="survey_users")
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="survey_user")
    answers = db.relationship("Answer", back_populates="user")
    has_reports = db.Column(db.Boolean)
    has_completed = db.Column(db.Boolean)
    current_group = db.relationship("Group", uselist=False)


class Category(BaseModel):
    __tablename__ = "categories"

    name = db.Column(db.String)
    groups = db.relationship("Group", back_populates="category")
    sequence = db.Column(db.Integer)

    survey_id = db.Column(db.Integer, db.ForeignKey("surveys.id"))
    survey = db.relationship("Survey", back_populates="categories")

    def __str__(self):
        return f"{self.id}-{self.sequence}--{self.name}"


class Group(BaseModel):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    sequence = db.Column(db.Integer)

    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    category = db.relationship("Category", back_populates="groups")

    next_group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))
    next_group = db.relationship(
        "Group",
        backref=db.backref("previous_group", remote_side=[id], uselist=False),
        uselist=False,
    )
    is_first = db.Column(db.Boolean)
    is_last = db.Column(db.Boolean)

    questions = db.relationship("Question", back_populates="group")

    current_user_id = db.Column(db.Integer, db.ForeignKey("survey_users.id"))

    def __str__(self):
        return f"{self.id}-{self.sequence}--{self.name}"


# Not working for unknown reason
# class ChoiceType(db.types.TypeDecorator):
#
#     impl = db.types.String
#
#     def __init__(self, choices, **kw):
#         self.choices = dict(choices)
#         super(ChoiceType, self).__init__(**kw)
#
#     def process_bind_param(self, value, dialect):
#         return [k for k, v in self.choices.items() if v == value][0]
#
#     def process_result_value(self, value, dialect):
#         return self.choices[value]


class Question(BaseModel):
    __tablename__ = "questions"

    label = db.Column(db.String)
    choices = db.Column(db.JSON)

    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))
    group = db.relationship("Group", back_populates="questions")
    answers = db.relationship("Answer", back_populates="question")
    type_id = db.Column(db.Integer, db.ForeignKey("question_types.id"))
    type = db.relationship("QuestionType", back_populates="questions")


class QuestionType(BaseModel):
    __tablename__ = "question_types"

    label = db.Column(db.String)
    questions = db.relationship("Question", back_populates="type")


class Answer(BaseModel):
    __tablename__ = "answers"

    statement = db.Column(db.String)
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"))
    question = db.relationship("Question", back_populates="answers")
    user_id = db.Column(db.Integer, db.ForeignKey("survey_users.id"))
    user = db.relationship("SurveyUser", back_populates="answers")
    type_id = db.Column(db.Integer, db.ForeignKey("answer_types.id"))
    type = db.relationship("AnswerType", back_populates="answers")


class AnswerType(BaseModel):
    __tablename__ = "answer_types"

    label = db.Column(db.String)
    answers = db.relationship("Answer", back_populates="type")
