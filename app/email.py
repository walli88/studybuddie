from threading import Thread
from flask import current_app, render_template
from flask.ext.mail import Message
from . import mail
import mandrill

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(subject,
                  sender=app.config['MAIL_USERNAME'], recipients=[to])
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr

def send_mandrill(to, subject):
    mandrill_client = mandrill.Mandrill('Wp4DNuztdO3KqDScxT2l0w')
    template_content = [{'content': 'example content', 'name': 'WelcomeEmail'}]
    message = {'from_email': 'support@studybuddie.me',
    'to': [{'email': to,
             'name': 'Recipient Name',
             'type': 'to'}],
     'subject': subject
    }
    result = mandrill_client.messages.send_template(message=message,template_name='WelcomeEmail',template_content=template_content)
    print result