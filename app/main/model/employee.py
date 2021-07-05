
from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt
from typing import Union


class Employee(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "employee"

    ID_EMPLOYEE = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NAME = db.Column(db.Text, nullable=False)
    PHOTO_EMPLOYEE = db.Column(db.Text, nullable=False)
    ADDRESS = db.Column(db.Text, nullable=False)
    AGE = db.Column(db.Integer, nullable=False)
    GENDER = db.Column(db.Text, nullable=False)
    ID_ADMIN = db.Column(db.Integer, db.ForeignKey('admin.id_admin'),
        nullable=False)