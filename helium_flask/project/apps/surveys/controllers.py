from flask import Blueprint, request
from flask_praetorian import auth_required, current_user

from helium_flask.project.apps.surveys.helpers import generate_questions_json
from helium_flask.project.apps.surveys.models import (
    Survey,
    SurveyUser,
    Group,
    Answer,
    AnswerType,
)
from helium_flask.project.apps.users.helpers import mail_login_token
from helium_flask.project.apps.users.models import User
from helium_flask.project.project.initialize_app import db

survey_router = Blueprint("survey_router", __name__)


@survey_router.route("surveys/", methods=["GET"])
@auth_required
def take_survey():
    survey_user = current_user().survey_user
    if survey_user.has_reports:
        if survey_user.has_completed:
            return {
                "message": "User has completed the survey, please take him to the report!"
            }
        else:
            return {"group_id": survey_user.current_group.id, "has_reports": True}
    else:
        return {"group_id": survey_user.current_group.id}


@survey_router.route("groups/<group_id>/")
@auth_required
def get_questions(group_id):
    return {"questions": generate_questions_json((Group.query.get(group_id)).questions)}


@survey_router.route("groups/<group_id>/<option>/", methods=["POST"])
@auth_required
def next_or_back(group_id, option):
    group = Group.query.get(group_id)
    type = AnswerType.query.filter_by(label="str").first()
    for answer in request.json.get("answers"):
        db.session.add(
            Answer(
                statement=answer.statement,
                question_id=answer.question_id,
                user=current_user.survey_user,
                type=type,
            )
        )
    db.session.commit()
    if option == "next":
        if group.is_last:
            current_user.survey_user.has_completed = True
            return {"message": "Survey completed!"}
        else:
            current_user.survey_user.current_group = group.next_group
            questions = generate_questions_json(group.next_group.questions)
            return {"group": group.next_group.id, "questions": questions}
    elif option == "back":
        if group.is_first:
            return {"message": "Survey completed!"}
        else:
            current_user.survey_user.current_group = group.previous_group
            questions = generate_questions_json(group.previous_group.questions)
            return {"group": group.previous_group.id, "questions": questions}


@survey_router.route("surveys/<survey_slug>/", methods=["POST"])
def organization_page(survey_slug):
    if survey := Survey.query.filter_by(slug=survey_slug).first():
        if request.json.get("pass_code") == survey.organization.pass_code:
            return {"message": "Success!"}
        else:
            return {"message": "Rejected!"}
    else:
        return {"message": "Invalid survey name!"}


@survey_router.route("<survey_slug>/invite/", methods=["POST"])
def invite_user(survey_slug):
    survey = Survey.query.filter_by(slug=survey_slug).first()
    email = request.json.get("email")
    user = User.query.filter_by(email=email).first()
    if user:
        return {"message": "User already exists!"}
    if mail_login_token(email):
        user = User(
            email=email,
            survey_user=SurveyUser(
                current_group=Group.query.filter_by(is_first=True)
                .filter(Group.category_id.in_([s.id for s in survey.categories]))
                .first(),
                survey=survey,
            ),
        )
        user.save()
        return {"message": "Mail sent and user created!"}
    else:
        return {"message": "Mail not sent!"}
