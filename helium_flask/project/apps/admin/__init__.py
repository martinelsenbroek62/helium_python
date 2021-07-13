# from helium_flask.project.helpers.const import SURVEY_INPUT_FIELD_TYPES
from helium_flask.project.helpers.generic_models import BaseModel


# from helium_flask.apps.users.models import user_survey_association
from helium_flask.project.project.initialize_app import db, admin

from flask_admin.contrib.sqla import ModelView

from helium_flask.project.apps.surveys.models import (
    Survey,
    SurveyUser,
    Organization,
    Question,
    Answer,
    Category,
    Group,
    QuestionType,
    AnswerType,
)
from helium_flask.project.apps.users.models import User

#
#
# from helium_flask.project.project.initialize_app import admin


# def create_admin(admin, db):
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Organization, db.session))
admin.add_view(ModelView(Survey, db.session))
admin.add_view(ModelView(SurveyUser, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Group, db.session))
admin.add_view(ModelView(Question, db.session))
admin.add_view(ModelView(QuestionType, db.session))
admin.add_view(ModelView(Answer, db.session))
admin.add_view(ModelView(AnswerType, db.session))
