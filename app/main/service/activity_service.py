from app.main import db
from flask import session
from app.main.model.activity import Activity
from app.main.model.category import Category
from datetime import datetime
import os

def insert_activity(data):
  try:
    
    token_session = session.get('token')
    name = data.get('name')

    data_category = Category.current_category()
    
    id_category = 99999
    if data_category:
      id_category = data_category.ID_CATEGORY

    id_employee = data.get('id_employee')
    time = datetime.now()
    id_admin = resp
    newActivity = Category(
      NAME = name,
      ID_CATEGORY = id_category,
      ID_EMPLOYEE = id_employee,
      TIME = time
    )
    db.session.add(newActivity)
    db.session.commit()

    if data_category:
      return data_category.NAME
    
    return 'late'
  except Exception as e:
    print(e)
    return False
