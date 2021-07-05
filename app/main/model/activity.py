
from .. import db, flask_bcrypt
from datetime import datetime
from app.main.model.category import Category
from app.main.model.employee import Employee
from ..config import key
import jwt
from typing import Union


class Activity(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "ACTIVITY"

    ID_ACTIVITY = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ID_CATEGORY = db.Column(db.Integer, db.ForeignKey('category.id_category'),
        nullable=False)
    ID_EMPLOYEE = db.Column(db.Integer, db.ForeignKey('employee.ID_EMPLOYEE'),
        nullable=False)
    TIME= db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def get_data_join():
        return db.session.query(
            Activity, Category, Employee
        ).filter(
            Activity.ID_CATEGORY == Category.ID_CATEGORY,
        ).filter(
            Activity.ID_EMPLOYEE == Employee.ID_EMPLOYEE,
        ).all()