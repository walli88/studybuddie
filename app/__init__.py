from flask import Flask, Blueprint
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from config import config
from mandrill import Mandrill


bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
mandrill = Mandrill()


def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	app.url_map.strict_slashes = False

	bootstrap.init_app(app)
	mail.init_app(app)
	db.init_app(app)
	from app.main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix='/auth')
	return app