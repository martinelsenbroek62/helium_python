from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, current_user, logout_user
from flask_mail import Message
from werkzeug.security import check_password_hash, generate_password_hash


survey_router = Blueprint('survey_router', __name__,
                        template_folder='../../templates/surveys')

@survey_router.route("get_started/")
def get_started():
    return render_template("get_started.html")


@survey_router.route("report/")
def report():
    return render_template("report.html")

@survey_router.route("take_survey/")
def take_survey():
    return render_template("take_survey.html")