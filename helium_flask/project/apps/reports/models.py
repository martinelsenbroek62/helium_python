from helium_flask.project.helpers.generic_models import BaseModel
from helium_flask.project.project.initialize_app import db


class UserReport(BaseModel):
    __tablename__ = "user_reports"
