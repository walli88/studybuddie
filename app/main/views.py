from flask import Flask, render_template, redirect, url_for, request, flash
from . import main
from ..auth.forms import LoginForm, SignUpForm, RegistrationForm
from .forms import StudentForm, TutorForm, GetHelpForm
from flask.ext.mail import Message
from .. import mail
from ..models import User, Tutor, Student
from app import db
from ..email import send_email, send_mandrill
from flask.ext.login import current_user, login_required


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

@main.route('/gethelp', methods=['GET', 'POST'])
@login_required
def gethelp():
	getHelpForm = GetHelpForm()
	if getHelpForm.validate_on_submit():
		getHelp = getHelp()
		print current_user
		print current_user.id
		# getHelp = GetHelp(st)
	return render_template('gethelp.html', getHelpForm=getHelpForm, hideLogin=True)


@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
	studentForm = StudentForm()
	if studentForm.validate_on_submit():
		student = Student(fullname=studentForm.fullName,school=studentForm.schoolName,
					grade=studentForm.grade,phonenumber=studentForm.phoneNumber,major=studentForm.major,user_id=current_user.id)
		if student is not None:
			db.session.add(student)
			db.session.commit()
	return render_template('profile.html', studentForm=studentForm, hideLogin=True)

@main.route('/tutors', methods=['GET', 'POST'])
def tutors():
	form = LoginForm()
	return render_template('tutors.html', form=form)

@main.route('/tutorprofile', methods=['GET', 'POST'])
@login_required
def tutorprofile():
	tutorForm = TutorForm()
	if request.method == 'GET' and request.args.get('email') is not None:
		tutorForm.email.data=request.args.get('email')
		send_mandrill(form.email.data, "Welcome to Studybuddie", 'TutorWelcomeEmail')

	if tutorForm.validate_on_submit():
		tutorForm = TutorForm()
		tutor = Tutor(fullname = tutorForm.fullName.data,school=tutorForm.school.data, grade=tutorForm.grade.data
			,major=tutorForm.major.data,gpa=float(tutorForm.gpa.data) if tutorForm.gpa.data != "(Optional)" else None
			,phonenumber=tutorForm.phonenumber.data,relexp=tutorForm.relexp.data)
		if tutor is not None and tutorForm.email.data:
			tutorDb = Tutor.query.filter_by(email=tutorForm.email.data).first()
			if tutorDb is None:
				db.session.add(tutor)
				db.session.commit()
				flash('Thanks for signing up!')
	return render_template('tutorprofile.html', tutorForm=tutorForm, hideLogin=True)


