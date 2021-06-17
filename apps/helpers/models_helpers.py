from sqlalchemy import Column, DateTime
from sqlalchemy.sql import functions

from helium_flask.apps.config import db

class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    time_created = Column(DateTime(timezone=True), default=functions.now()) #todo: search on this.
    time_updated = Column(DateTime(timezone=True), default=functions.now(), onupdate=functions.now())

    def getall(self):
        self
    def save(self):
        # self.before_save()
        db.session.add(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    def delete(self):
        db.session.delete(self)
        db.session.commit()