from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, current_user, logout_user
from flask_mail import Message
from werkzeug.security import check_password_hash, generate_password_hash


claim_router = Blueprint('claim_router', __name__,
                        template_folder='../templates/claims')

@claim_router.route("reimburse/")
def reimburse():
    return render_template("reimburse.html")
