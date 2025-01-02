from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from route.user_route import user_bp
from route.user_route import admin_bp
from route.auth_route import auth_bp
from route.courses_route import courses_bp
from route.courses_route import user_course_bp
from middleware.error_handler import error_handler
from model import db

app = Flask(__name__)
app.json.sort_keys = False
CORS(app)

# Konfigurasi aplikasi
app.config.from_object('config')
jwt = JWTManager(app)

# Inisialisasi database dan migrasi
db.init_app(app)
migrate = Migrate(app, db)

#Regis route
app.register_blueprint(user_bp, url_prefix='/api/v1')
app.register_blueprint(admin_bp, url_prefix='/api/v1')
app.register_blueprint(auth_bp, url_prefix='/api/v1')
app.register_blueprint(courses_bp, url_prefix='/api/v1')
app.register_blueprint(user_course_bp, url_prefix='/api/v1')

# Registrasi handler untuk error
error_handler(app)

# gunakan saat local development
if __name__ == '__main__':
    app.run(port=5000)