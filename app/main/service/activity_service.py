from app.main import db
from flask import session
from app.main.model.activity import Activity
from app.main.model.category import Category
from datetime import datetime
import os

def insert_activity(data):
  try:
    
    token_session = session.get('token')
    name = data.args.get('name')

    data_category = Category.current_category()
    
    id_category = 3
    if data_category:
      id_category = data_category.ID_CATEGORY

    id_employee = data.args.get('id_employee')
    time = datetime.now()
    newActivity = Activity(
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

def get_all_activity(): 
  return Activity.get_data_join()