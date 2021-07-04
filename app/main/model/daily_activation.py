
from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt
from typing import Union


class DAILY_ACTIVATION(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "DAILY_ACTIVATION"

    ID_DAILY_ACTIVATION = db.Column(db.Integer, primary_key=True, autoincrement=True)
    STATUS = db.Column(db.Integer)
    DATE = db.Column(db.DateTime, nullable=False)
    ID_ADMIN = db.Column(db.Integer, db.ForeignKey('admin.id_admin'),
        nullable=False)
    