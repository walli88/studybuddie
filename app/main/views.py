from flask import Flask, render_template, redirect, url_for, request, flash
from . import main
from ..auth.forms import LoginForm, SignUpForm, RegistrationForm
from .forms import StudentForm, TutorForm, GetHelpForm, ScheduleForm
from flask.ext.mail import Message
from .. import mail
from ..models import User, Tutor, Student, GetHelp
from app import db
from ..email import send_email, send_mandrill
from flask.ext.login import current_user, login_required

@main.route('/dashboard', methods=['GET','POST'])
@login_required
def dashboard():
	student = Student.query.filter_by(user_id=current_user.id).first()
	schoolMap = {'colm':'Columbia University', 'nyu':'New York University'}
	fullname = None;
	Schoolname = None;
	if student is not None:
		fullname = student.fullname
		schoolname = schoolMap[student.school]
	getHelps = GetHelp.query.all()
	return render_template('dashboard.html',FirstName=fullname,SchoolName=Schoolname,getHelps=getHelps)

@main.route('/tutordashboard', methods=['GET', 'POST'])
def tutordashboard():
	return render_template('tutordashboard.html')

@main.route('/', methods=['GET', 'POST'])
def index():
	loginForm = LoginForm()
	signUpForm = SignUpForm()
	registerForm = RegistrationForm()
	if current_user.is_authenticated():
		return redirect(url_for('main.dashboard'))
		# return render_template('index.html', signUpForm=signUpForm,loginForm=loginForm,registerForm=registerForm)
	else:
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
		student = Student.query.filter_by(user_id=current_user.id).first()
		if student is not None:
			getHelp = GetHelp(class_number=getHelpForm.classNumber.data,location=getHelpForm.location.data,help_comment=getHelpForm.helpComment.data,
				duration=getHelpForm.duration.data,student=student)
			if getHelp is not None:
				db.session.add(getHelp)
				db.session.commit()
			return redirect(url_for('main.dashboard'))
	return render_template('gethelp.html', getHelpForm=getHelpForm, hideLogin=True)


@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
	student = Student.query.filter_by(user_id=current_user.id).first()
	studentForm = StudentForm(request.form,obj=student)
	if student is not None:
		studentForm.submit.label.text='Edit'
	if studentForm.validate_on_submit():
		if student is not None:
			student.fullname = studentForm.fullname.data
			student.school =  studentForm.school.data
			student.grade = studentForm.grade.data
			student.phonenumber = studentForm.phonenumber.data
			student.major = studentForm.major.data
			db.session.merge(student)
			db.session.commit()
		else:
			student = Student(fullname=studentForm.fullname.data,school=studentForm.school.data,
					grade=studentForm.grade.data,phonenumber=studentForm.phonenumber.data,major=studentForm.major.data,user=current_user._get_current_object())
			db.session.add(student)
			db.session.commit()
		return redirect(url_for('main.profile'))
	return render_template('profile.html', studentForm=studentForm)

@main.route('/tutors', methods=['GET', 'POST'])
def tutors():
	signUpForm = SignUpForm()
	return render_template('tutors.html', tutor=True, signUpForm=signUpForm)

@main.route('/tutorprofile', methods=['GET', 'POST'])
@login_required
def tutorprofile():
	tutor = Tutor.query.filter_by(user_id=current_user.id).first()
	student = Student.query.filter_by(user_id=current_user.id).first()
	tutorForm = TutorForm(request.form,obj=tutor)

	if student is not None and tutor is None:
		tutorForm.fullname.data = student.fullname
		tutorForm.school.data = student.school
		tutorForm.grade.data = student.grade
		tutorForm.major.data = student.major
		tutorForm.phonenumber.data = student.phonenumber

	if tutor is not None:
		tutorForm.submit.label.text='Edit'

	if tutorForm.validate_on_submit():
		print "tutorForm validated"
		if tutor is not None:
			tutor.fullname = tutorForm.fullname.data
			tutor.school =  tutorForm.school.data
			tutor.grade = tutorForm.grade.data
			tutor.phonenumber = tutorForm.phonenumber.data
			tutor.major = tutorForm.major.data
			db.session.merge(tutor)
			db.session.commit()
			flash('Your tutor profile has been updated!')
		else:
			tutor = Tutor(fullname = tutorForm.fullname.data, user_id = current_user.id, school=tutorForm.school.data, grade=tutorForm.grade.data
				,major=tutorForm.major.data,gpa=float(tutorForm.gpa.data) if tutorForm.gpa.data != "(Optional)" else None
				,phonenumber=tutorForm.phonenumber.data,relexp=tutorForm.relexp.data)
			db.session.add(tutor)
			db.session.commit()
			flash('Thanks for signing up to be a tutor!')
		return redirect(url_for('main.tutorprofile'))
	return render_template('tutorprofile.html', tutorForm=tutorForm, hideLogin=True)

@main.route('/schedule', methods=['GET', 'POST'])
def schedule():
	scheduleForm = ScheduleForm()
	return render_template('schedule.html', tutor=True,scheduleForm=scheduleForm)