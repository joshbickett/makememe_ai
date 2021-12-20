from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import json

with open('/etc/make_meme/config.json') as config_file:
    config = json.load(config_file)

app = Flask(__name__)
app.config['SECRET_KEY'] = config["SECRET_KEY"]
# CORS(app)

app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = config["DB_URI"]
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from makememe import routes
from makememe import make