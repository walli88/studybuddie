from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,SubmitField, IntegerField, DecimalField, DateField, DateTimeField
from wtforms.validators import Required, Length, Email, Regexp, NumberRange, Optional
from wtforms import ValidationError
from ..models import User
import re
import datetime as dt

def validatePhone(form, field):
    if field.data != "(Optional)" and (len(field.data) !=10 or re.match("^[0-9]*$",field.data) is None):
        raise ValidationError("Telephone should be 10 digits (no spaces)")


class GetHelpForm(Form):
    className = StringField('Class', validators=[Required(), Length(0, 64)])
    professor = StringField('Professor', validators=[Required(), Length(0, 64)])
    location = StringField('Where do you want the study session to take place?', validators=[Required(), Length(0, 64)])
    needHelp = StringField('What do you need help in?',placeholder='(Optional)') 
    howLongSession = SelectField(u'Minutes', default = '30', choices=[('30', '30 min'),('60', '60 min'), ('90', '90 min'),('120', '120 min')],validators=[Required()])
    whenStartDay = DateField('Start date (i.e 3/16/2015)?',format='%m/%d/%Y', default=dt.datetime.now)
    whenStartTime = DateTimeField('Start time (00:00-23:59)?',format='%H:%M', default= dt.datetime.now() + dt.timedelta(hours=1))
    submit = SubmitField()

class FindClassForm(Form):
    studentName = StringField('Name', validators=[Required(message="Name is required"),Length(0,64)])
    schoolName  = SelectField(u'School', default='none', choices=[('none', 'Please select your school'), ('colm', 'Columbia University'), ('nyu', 'New York University')
        , ('other', 'Other')])
    yearName = SelectField(u'Year', default='none', choices=[('none', 'Please select your year'), ('fr', 'Freshman'), ('soph', 'Sophmore'), ('jr','Junior',),('sr','Senior'),('oth','Grad Student')
        , ('other', 'Other')])
    phoneNumber = StringField('Phone Number: StudyBuddies call/text when they arrive', validators=[Length(0, 64)])
    majorName = StringField('Major')
    submit = SubmitField()

class StudentForm(Form):
    className = StringField('Class', validators=[Length(0, 64)])
    professor = StringField('Professor', validators=[Length(0, 64)])
    phoneNumber = StringField('Phone Number', validators=[Length(0, 64)])
    needHelp = StringField('What do you need help in?')
    howLongSession = StringField('How long would this session take?')
    submit = SubmitField()

class TutorForm(Form):
    fullName = StringField('Full Name', validators=[Required(), Length(1, 64)])
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    school  = SelectField(u'School', default='none', choices=[('none', 'Please select your school'), ('colm', 'Columbia University'), ('fordham', 'Fordham University'), ('hunter', 'Hunter University'), ('nyu', 'New York University'), ('pace', 'Pace University'), ('cunyq', 'Queens College, CUNY')
        , ('other', 'Other')])
    grade = SelectField(u'Grade', default = 'none', choices=[('none', 'Please select your grade'),('fresh', 'Freshman'), ('soph', 'Sophmore'), ('junior', 'Junior'),('senior', 'Senior'),
        ('grad', 'Masters'),('phd', 'Ph.D'),('alum', 'Alumni')])
    major = StringField('Major', default='(Optional)',validators=[Length(0, 64)])
    gpa = DecimalField("Bachelor's GPA", validators=[NumberRange(min=0,max=4,message="Please enter a value between 0.0 and 4.0"), Optional()])
    phonenumber = StringField('Phone',default='(Optional)', validators=[validatePhone])
    relexp = TextAreaField('Relevant Experience', default='(Optional)',validators=[Length(0,500)])
    submit = SubmitField()

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

class EditProfileForm(Form):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class EditProfileAdminForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

class CommentForm(Form):
    body = StringField('Enter your comment', validators=[Required()])
    submit = SubmitField('Submit')
