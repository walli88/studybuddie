from flask import render_template
from . import main
from ..auth.forms import LoginForm
from flask.ext.mail import Message
from .. import mail

@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    user = form.email.data
    if user is not None:
        msg = Message("Welcome to Studybuddie",
                      sender="support@studybuddie.me",
                      recipients=[user])
        msg.body = "Thanks for signing up for studybuddie! We will let you know as soon as we lauch!"
        mail.send(msg)
    return render_template('index.html', form=form)