from flask import render_template, redirect, url_for
from . import auth
from .forms import LoginForm
from ..models import User
from .. import mail
from app import db
from flask.ext.mail import Message
from ..email import send_email, send_mandrill

@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = LoginForm()
	user = User(email=form.email.data,
					password_hash=form.password.data)

	if user is not None and form.email.data:
		userDb = User.query.filter_by(email=form.email.data).first()
		# if userDb is not None:
			#print "userDb something different" + ":" + userDb.email
		if userDb is None:
			db.session.add(user)
			db.session.commit()
		#send_email(user.email,"Welcome to Studybuddie", "email")
		send_mandrill(user.email, "Welcome to Studybuddie", 'WelcomeEmail')
	return redirect(url_for('main.signedup'))

@auth.route('/registertutor', methods=['GET', 'POST'])
def registertutor():
	form = LoginForm()
	return redirect(url_for('main.tutorprofile', email=form.email.data	))
