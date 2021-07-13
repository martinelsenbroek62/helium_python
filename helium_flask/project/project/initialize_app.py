from flask import Flask
from flask_admin import Admin
from flask_cors import CORS
from flask_mail import Mail
from flask_praetorian import Praetorian

from helium_flask.project.helpers.app_setup_helpers import (
    initialize_db,
    configure_app,
)

app = Flask(__name__)
CORS(app)
app = configure_app(app)
db = initialize_db(app)
admin = Admin(app, name="Sustainabli", template_mode="bootstrap3")
mail = Mail(app)
guard = Praetorian()
