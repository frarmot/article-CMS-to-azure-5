"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
logger=logging.getLogger('azure')
logger.setLevel(logging.INFO)
app.logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
#logger = logging.getLogger('azure')
#logger.setLevel(logging.INFO)
#handler = logging.StreamHandler()
#logger.addHandler(handler)
#app.logger.setLevel(logging.INFO)
#
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
