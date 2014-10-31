import os
import json
from flask import Flask, request, Response
from flask import render_template, send_from_directory, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail, Message
from flask.ext.migrate import Migrate, MigrateCommand


bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
app = Flask(__name__)
bootstrap.init_app(app)
mail.init_app(app)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "support@studybuddie.me"
app.config['MAIL_PASSWORD'] = "tuber2014"

import angular_flask.controllers


def create_app():
	app = Flask(__name__)
	# app.config.from_object('angular_flask.settings')
	app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
	app.config['MAIL_PORT'] = 587
	app.config['MAIL_USE_TLS'] = True
	app.config['MAIL_USERNAME'] = "support@studybuddie.me"
	app.config['MAIL_PASSWORD'] = "tuber2014"

	# app.config.from_object(config[config_name])
	# config[config_name].init_app(app)
	bootstrap.init_app(app)
	mail.init_app(app)
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	# moment.init_app(app)
	# db.init_app(app)
	# login_manager.init_app(app)
	# pagedown.init_app(app)
	return app