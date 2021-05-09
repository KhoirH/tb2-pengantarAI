import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

UPLOAD_FOLDER = 'dataset'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])