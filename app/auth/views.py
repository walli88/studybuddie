from flask import render_template, redirect, url_for, flash, request
from . import auth
from .forms import LoginForm, SignUpForm, RegistrationForm
from ..models import User, SignUp
from .. import mail
from app import db
from flask.ext.mail import Message
from ..email import send_email, send_mandrill
from flask.ext.login import login_user, logout_user, login_required, current_user
import ast

@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if request.args.get('email') is not None:
		form.email.data=request.args.get('email')
	if request.args.get('tutor') is not None:
		form.isstudent.data = not ast.literal_eval(request.args.get('tutor'))
		form.istutor.data = ast.literal_eval(request.args.get('tutor'))

	if form.validate_on_submit():
		user = User(email=form.email.data,
					password=form.password.data)
		if user is not None and form.email.data:
			userDb = User.query.filter_by(email=form.email.data).first()
			if userDb is None:
				db.session.add(user)
				db.session.commit()
			login_user(user)
			return redirect(url_for('main.profile'))
	return render_template('auth/register.html', form=form, hideLogin=True, email=form.email.data)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
	signUpForm = SignUpForm()
	if request.args.get('tutor') is not None:
		tutor=request.args.get('tutor')
	signUp = SignUp(email=signUpForm.email.data)
	if signUp is not None and signUpForm.email.data:
		signUpDb = signUp.query.filter_by(email=signUpForm.email.data).first()
		if signUpDb is None:
			db.session.add(signUp)
			db.session.commit()
		send_mandrill(signUp.email, "Welcome to Studybuddie", 'WelcomeEmail')
	return redirect(url_for('auth.register', tutor=tutor, email=signUpForm.email.data))

@auth.route('/registertutor', methods=['GET', 'POST'])
def registertutor():
	form = LoginForm()
	user = User(email=form.email.data)
	return redirect(url_for('main.tutorprofile', email=form.email.data))

@auth.route('/registerstudent', methods=['GET', 'POST'])
def registerstudent():
	form = LoginForm()
	user = User(email=form.email.data)
	return redirect(url_for('main.tutorprofile', email=form.email.data))

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(url_for('main.profile'))
		flash('Invalid username or password.')
		return redirect(url_for('auth.login'))
	return render_template('auth/login.html', form=form, hideLogin=True)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))