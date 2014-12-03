from flask import render_template
from . import main
from ..auth.forms import LoginForm
from .forms import FindClassForm
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


@main.route('/aboutus', methods=['GET', 'POST'])
def aboutus():
    form = LoginForm()
    return render_template('aboutus.html', form=form)