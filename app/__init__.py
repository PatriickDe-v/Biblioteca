from flask import Flask  # set FLASK_APP=biblioteca.py Inicia o servidor.
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

# Inicialização do banco de dados 
app = Flask(__name__) 
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

login = LoginManager(app)
login.login_view = 'login'

from app import models, routes
