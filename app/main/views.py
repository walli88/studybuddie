from flask import Flask, render_template, redirect, url_for, request
from . import main
from ..auth.forms import LoginForm
from .forms import FindClassForm,TutorForm
from flask.ext.mail import Message
from .. import mail
from ..models import User, Tutor
from app import db
from ..email import send_email

@main.route('/', methods=['GET', 'POST'])
def index():
	form = LoginForm()
	return render_template('index.html', form=form)

@main.route('/signedup', methods=['GET', 'POST'])
def signedup():
	form = LoginForm()
	return render_template('index2.html', form=form)


@main.route('/profile', methods=['GET', 'POST'])
def profile():
	form = FindClassForm()
	return render_template('profile.html', form=form)

@main.route('/tutors', methods=['GET', 'POST'])
def tutors():
	form = LoginForm()
	return render_template('tutors.html', form=form)

@main.route('/tutorprofile', methods=['GET', 'POST'])
def tutorprofile():
	form = TutorForm()
	if request.method == 'GET' and request.args.get('email') is not None:
		form.email.data=request.args.get('email')
	if form.validate_on_submit():
		print "validate"
		form = TutorForm()
		tutor = Tutor(fullname = form.fullName.data, email=form.email.data
			,school=form.school.data, grade=form.grade.data
			,major=form.major.data,gpa=form.major.data if form.major.data != "(Optional)" else None
			,phonenumber=form.phonenumber.data,relexp=form.relexp.data)
		if tutor is not None and form.email.data:
			print "tutor is not None"
			print "email" + ":" + form.email.data
			tutorDb = Tutor.query.filter_by(email=form.email.data).first()
			if tutorDb is not None:
				print "tutorDb email" + ":" + tutorDb.email
			print "afterDb"
			if tutorDb is None:
				print "tutordb is None"
				print db.session.add(tutor)
				db.session.commit()
	return render_template('tutorprofile.html', form=form)