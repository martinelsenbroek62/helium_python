from flask_migrate import Migrate
from helium_flask.project.project.initialize_app import app, db
from helium_flask.project.apps.claims.models import Claims
migrate = Migrate(app, db)
