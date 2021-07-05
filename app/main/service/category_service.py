from app.main import db
from app.main.model.category import Category

def status_category():
  return Category.current_category()