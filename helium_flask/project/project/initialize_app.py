from flask import Flask

from helium_flask.project.helpers.app_setup_helpers import initialize_db, configure_app, initialize_login_manager

app = Flask(__name__, static_folder="../static", template_folder="../templates")
app = configure_app(app)
db = initialize_db(app)
login_manager = initialize_login_manager(app)