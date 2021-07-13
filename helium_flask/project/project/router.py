from flask import url_for, redirect

from helium_flask.project.project.initialize_app import app
from helium_flask.project.apps.users.controllers import user_router
from helium_flask.project.apps.surveys.controllers import survey_router
from helium_flask.project.apps.admin.controllers import admin_router
from helium_flask.project.apps.claims.controllers import claim_router
from helium_flask.project.apps.reports.controllers import report_router

app.register_blueprint(user_router, url_prefix="/")
app.register_blueprint(survey_router, url_prefix="/")
app.register_blueprint(admin_router, url_prefix="/")
app.register_blueprint(report_router, url_prefix="/")
app.register_blueprint(claim_router, url_prefix="/")
