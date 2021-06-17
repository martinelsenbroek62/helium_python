from helium_flask.apps.config import app
from helium_flask.apps.users.controllers import user_router
from helium_flask.apps.general.controllers import general_router
from helium_flask.apps.surveys.controllers import survey_router
from helium_flask.apps.admin.controllers import admin_router
from helium_flask.apps.claims.controllers import claim_router
from helium_flask.apps.reports.controllers import report_router

app.register_blueprint(user_router, url_prefix="/users/")
app.register_blueprint(general_router, url_prefix="/general/")
app.register_blueprint(survey_router, url_prefix="/surveys/")
app.register_blueprint(admin_router, url_prefix="/admin/")
app.register_blueprint(report_router, url_prefix="/report/")
app.register_blueprint(claim_router, url_prefix="/claim/")


