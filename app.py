from flask import Flask
from database import db
from encriptador import bcrypt
from flask_migrate import Migrate
from config import BasicConfig
from flask_cors import CORS
from routes.user.user import appuser
from routes.images.images import imageUser
from routes.pdf.pdf import apppdf
from routes.csv.csv import appcsv
app = Flask(__name__)
app.register_blueprint(appuser)
app.register_blueprint(imageUser)
app.register_blueprint(apppdf)
app.register_blueprint(appcsv)
app.config.from_object(BasicConfig)
CORS(app)
bcrypt.init_app(app)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)