from flask import Blueprint, render_template
from flask_login import login_required


general_router = Blueprint('general_router', __name__,
                        template_folder='../templates/general')

@general_router.route("home/")
@login_required
def home():
    return render_template("home.html")

