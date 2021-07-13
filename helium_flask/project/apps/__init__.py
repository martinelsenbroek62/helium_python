from flask_migrate import Migrate

# from helium_flask.project.apps.surveys.models import Survey
# from helium_flask.project.apps.users.models import User
from helium_flask.project.project.initialize_app import app, db

migrate = Migrate(app, db)
