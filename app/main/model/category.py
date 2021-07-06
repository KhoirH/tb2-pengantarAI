
from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt
from typing import Union
from app.main.util.time import between_time
from datetime import datetime

class Category(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "category"

    ID_CATEGORY = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NAME = db.Column(db.Text, nullable=False)
    START_TIME = db.Column(db.Text, nullable=False)
    END_TIME = db.Column(db.Text, nullable=False)
    ID_ADMIN = db.Column(db.Integer, db.ForeignKey('admin.id_admin'),
        nullable=False)
    

    @staticmethod
    def current_category() :
        categories = Category.query.all()
        data = False
        for category in categories:
            status = between_time(datetime.now(), category.START_TIME, category.END_TIME)
            if status :
                data = category
                break
            
        return data

