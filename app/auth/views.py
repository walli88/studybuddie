from flask import render_template
from . import auth
from .forms import LoginForm
from ..models import User
from .. import mail
from app import db
from flask.ext.mail import Message

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	user = User(email=form.email.data,
					password_hash=form.password.data)
	if user is not None and form.email.data is not None:
		db.session.add(user)
		db.session.commit()
		msg = Message("Welcome to Studybuddie",
					  sender="support@studybuddie.me",
					  recipients=[user.email])
		msg.body = "Thanks for signing up for studybuddie! We will let you know as soon as we lauch!"
		mail.send(msg)
	return render_template('index.html', form=form)
