from flask import Flask, Blueprint
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from config import config
from mandrill import Mandrill
from flask.ext.login import LoginManager
from flask_wtf.csrf import CsrfProtect

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
mandrill = Mandrill()
csrf = CsrfProtect()


def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	app.url_map.strict_slashes = False

	bootstrap.init_app(app)
	mail.init_app(app)
	db.init_app(app)
	csrf.init_app(app)
	login_manager.init_app(app)
	from app.main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix='/auth')
	return app