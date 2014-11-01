from flask import render_template
from . import main
from ..auth.forms import LoginForm
from flask.ext.mail import Message
from .. import mail
from ..models import User
from app import db

@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    user = User(email=form.email.data,
                    password_hash=form.password.data)
    if user is not None and form.email.data is not None:
        # db.session.add(user)
        # db.session.commit()
        msg = Message("Welcome to Studybuddie",
                      sender="support@studybuddie.me",
                      recipients=[user.email])
        msg.body = "Thanks for signing up for studybuddie! We will let you know as soon as we lauch!"
        mail.send(msg)
    return render_template('index.html', form=form)