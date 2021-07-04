from app.main import db
from flask import session
from app.main.model.employee import Employee
from app.main.model.admin import Admin
from typing import Dict, Tuple
from werkzeug.utils import secure_filename
import os

def insert_employee(data):
  try:
    token_session = session.get('token')
    resp = Admin.decode_auth_token(token_session)
    name = data.form.get('name')
    address = data.form.get('address')
    age = data.form.get('age')
    gender = data.form.get('gender')
    file = data.files['file']
    filename = secure_filename(file.filename)
    ext = filename.rsplit('.', 1)[1].lower()
    last_data = db.session.query(Employee).order_by(Employee.ID_EMPLOYEE.desc()).first()
    photo_employee = os.path.join('app\main\dataset',  str(last_data.ID_EMPLOYEE + 1) + '.' + ext)
    file.save(photo_employee)
          
    id_admin = resp
    newEmployee = Employee(
      NAME = name,
      ADDRESS = address,
      AGE = age,
      GENDER = gender,
      PHOTO_EMPLOYEE = photo_employee,
      ID_ADMIN = resp
    )
    db.session.add(newEmployee)
    db.session.commit()
    return True
  except Exception as e:
    print(e)
    return False

def get_all_employee():
  return Employee.query.all()