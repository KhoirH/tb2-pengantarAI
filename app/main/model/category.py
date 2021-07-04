
from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt
from typing import Union


class CATEGORY(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "CATEGORY"

    ID_CATEGORY = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NAME = db.Column(db.Text, nullable=False)
    START_TIME = db.Column(db.DateTime)
    END_TIME = db.Column(db.DateTime)
    TIME= db.Column(db.DateTime, default=datetime.utcnow)
    ID_ADMIN = db.Column(db.Integer, db.ForeignKey('admin.id_admin'),
        nullable=False)
