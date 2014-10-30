import os
import json
from flask import Flask, request, Response
from flask import render_template, send_from_directory, url_for
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail, Message

bootstrap = Bootstrap()
mail = Mail()

app = Flask(__name__)



app.config.from_object('angular_flask.settings')
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "support@studybuddie.me"
app.config['MAIL_PASSWORD'] = "tuber2014"
bootstrap.init_app(app)
mail.init_app(app)



app.url_map.strict_slashes = False

import angular_flask.core
import angular_flask.models
import angular_flask.controllers

