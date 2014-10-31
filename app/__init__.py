from flask import Flask, Blueprint
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()


def create_app():
	app = Flask(__name__)
	app.config.from_object('app.settings')
	app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
	app.config['MAIL_PORT'] = 587
	app.config['MAIL_USE_TLS'] = True
	app.config['MAIL_USERNAME'] = "support@studybuddie.me"
	app.config['MAIL_PASSWORD'] = "tuber2014"
	app.url_map.strict_slashes = False

	bootstrap.init_app(app)
	mail.init_app(app)
	from app.main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	return app