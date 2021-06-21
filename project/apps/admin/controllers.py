from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, current_user, logout_user
from flask_mail import Message
from werkzeug.security import check_password_hash, generate_password_hash


admin_router = Blueprint('admin_router', __name__,
                        template_folder='../../templates/admin')

