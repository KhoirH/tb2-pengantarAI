from app.main import db
from flask import session
from app.main.model.category import Category

def status_category():
  return Category.current_category()

def get_all_category():
  return Category.query.all()