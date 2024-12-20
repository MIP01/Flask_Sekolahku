from flask import Flask
from flask_cors import CORS
from route.user_routes import user_bp
from flask_migrate import Migrate
from model import db

app = Flask(__name__)
CORS(app)
app.json.sort_keys = False

#Migrate func
app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)

#Regis route
app.register_blueprint(user_bp, url_prefix='/api/v1')

# gunakan saat local development
if __name__ == '__main__':
    app.run(port=5000)