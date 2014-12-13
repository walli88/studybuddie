from flask import render_template, redirect, url_for, request
from . import main
from ..auth.forms import LoginForm
from .forms import FindClassForm,TutorForm
from flask.ext.mail import Message
from .. import mail
from ..models import User
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
    form.email.data=request.args.get('email')
    if form.validate_on_submit():
		print "validate"
    return render_template('tutorprofile.html', form=form)