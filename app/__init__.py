from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
DB = SQLAlchemy(app)
migrate = Migrate(app, DB)

from app import views