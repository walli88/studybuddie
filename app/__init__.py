from flask import Flask, Blueprint
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from config import config

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()


def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	app.url_map.strict_slashes = False

	bootstrap.init_app(app)
	mail.init_app(app)
	from app.main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	return app