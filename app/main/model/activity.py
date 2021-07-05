
from .. import db, flask_bcrypt
from datetime import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt
from typing import Union


class Activity(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "ACTIVITY"

    ID_ACTIVITY = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ID_CATEGORY = db.Column(db.Integer, db.ForeignKey('category.id_category'),
        nullable=False)
    ID_EMPLOYEEE = db.Column(db.Integer, db.ForeignKey('employee.id_employee'),
        nullable=False)
    TIME= db.Column(db.DateTime, default=datetime.utcnow)
