from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import getenv

db = SQLAlchemy()
mail = None
app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = getenv("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

db.init_app(app)
migrate = Migrate(app, db)
from helium_flask.apps.users.models import User
login_manager = LoginManager()
login_manager.login_view = 'user_router.login'
login_manager.init_app(app)
mail = Mail(app)

from helium_flask.apps.users.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from itsdangerous import URLSafeTimedSerializer


ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])

    # app.config.from_object(os.environ['APP_SETTINGS'])
