from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import routes


def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db = SQLAlchemy(app)
  Migrate(app, db)
  routes.init_app(app)

  return app