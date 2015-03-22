from flask import Flask, render_template, redirect, url_for, request, flash
from . import main
from ..auth.forms import LoginForm, SignUpForm, RegistrationForm
from .forms import FindClassForm,TutorForm
from flask.ext.mail import Message
from .. import mail
from ..models import User, Tutor
from app import db
from ..email import send_email, send_mandrill

@main.route('/', methods=['GET', 'POST'])
def index():
	loginForm = LoginForm()
	signUpForm = SignUpForm()
	registerForm = RegistrationForm()
	return render_template('index.html', signUpForm=signUpForm,loginForm=loginForm,registerForm=registerForm)

@main.route('/aboutus', methods=['GET', 'POST'])
def aboutus():
	return render_template('aboutus.html')


@main.route('/signedup', methods=['GET', 'POST'])
def signedup():
	loginForm = LoginForm()
	signUpForm = SignUpForm()
	return render_template('index2.html', loginForm=loginForm,signUpForm=signUpForm)


@main.route('/profile', methods=['GET', 'POST'])
def profile():
	findClassForm = FindClassForm()
	findClassForm.validate_on_submit()



	return render_template('profile.html', findClassForm=findClassForm, hideLogin=True)

@main.route('/tutors', methods=['GET', 'POST'])
def tutors():
	form = LoginForm()
	return render_template('tutors.html', form=form)

@main.route('/tutorprofile', methods=['GET', 'POST'])
def tutorprofile():
	form = TutorForm()
	if request.method == 'GET' and request.args.get('email') is not None:
		form.email.data=request.args.get('email')
		send_mandrill(form.email.data, "Welcome to Studybuddie", 'TutorWelcomeEmail')

	if form.validate_on_submit():
		form = TutorForm()
		tutor = Tutor(fullname = form.fullName.data, email=form.email.data
			,school=form.school.data, grade=form.grade.data
			,major=form.major.data,gpa=float(form.gpa.data) if form.gpa.data != "(Optional)" else None
			,phonenumber=form.phonenumber.data,relexp=form.relexp.data)
		if tutor is not None and form.email.data:
			tutorDb = Tutor.query.filter_by(email=form.email.data).first()
			if tutorDb is None:
				db.session.add(tutor)
				db.session.commit()
				flash('Thanks for signing up!')
	return render_template('tutorprofile.html', form=form, hideLogin=True)


