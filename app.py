from flask import Flask
from flask_cors import CORS
from route.user_routes import user_bp
from flask_migrate import Migrate
from model import db
from middleware.error_handler import error_handler
from middleware.logs import init_logging_middleware


app = Flask(__name__)
CORS(app)
app.json.sort_keys = False
port = 5000

# Initialize logging middleware
init_logging_middleware(app)

#Migrate func
app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)

#Regis route
app.register_blueprint(user_bp, url_prefix='/api/users')

# Registrasi handler untuk error
error_handler(app)

if __name__ == '__main__':
    app.debug = True
    app.logger.info(f"Server berhasil di running di http://localhost:{port}")
    app.run(port=port)