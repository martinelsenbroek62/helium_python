from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer

from helium_flask.project.apps.users.models import User
from helium_flask.project.project.initialize_app import app, login_manager

ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])

mail = Mail(app)


login_manager.login_view = 'user_router.login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
