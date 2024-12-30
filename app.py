from flask import Flask
from flask_cors import CORS
from route.user_routes import user_bp
from flask_migrate import Migrate
from middleware.error_handler import error_handler
from model import db

app = Flask(__name__)
app.json.sort_keys = False
CORS(app)

#Migrate func
app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)

#Regis route
app.register_blueprint(user_bp, url_prefix='/api/v1')

# Registrasi handler untuk error
error_handler(app)

# gunakan saat local development
if __name__ == '__main__':
    app.run(port=5000)