import os
import pymysql
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

load_dotenv()
pymysql.install_as_MySQLdb()

# JWT Config
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

# Each Flask web application contains a secret key which used to sign session cookies for protection against cookie data tampering.
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode, that will refresh the page when you make changes.
DEBUG = True

# Connect to the MYSQL database
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace('mysql://', 'mysql+pymysql://')

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False