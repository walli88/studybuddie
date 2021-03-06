from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,SubmitField, IntegerField, DecimalField, DateField, DateTimeField
from wtforms.validators import Required, Length, Email, Regexp, NumberRange, Optional
from wtforms import ValidationError, widgets
from ..models import User
import re
import datetime as dt

def validatePhone(form, field):
    if field.data != "(Optional)" and (len(field.data) !=10 or re.match("^[0-9]*$",field.data) is None):
        raise ValidationError("Telephone should be 10 digits (no spaces)")

class GetHelpForm(Form):
    classNumber = StringField('Class Number', validators=[Required(), Length(0, 64)])
    location = StringField('Where do you want the study session to take place?', validators=[Required(), Length(0, 64)])
    helpComment = StringField('What do you need help in?')
    duration = SelectField(u'Minutes', default = '30', choices=[('30', '30 min'),('60', '60 min'), ('90', '90 min'),('120', '120 min')],validators=[Required()])
    whenStartDay = DateField('Start date (i.e 3/16/2015)?',format='%m/%d/%Y', default=dt.datetime.now)
    whenStartTime = DateTimeField('Start time (00:00-23:59)?',format='%H:%M', default= dt.datetime.now() + dt.timedelta(hours=1))
    submit = SubmitField()

class ScheduleForm(Form):
    date = DateField('Week of? (Any day in the week will do)',format='%m/%d/%Y', default=dt.datetime.now)
    mon = BooleanField('Monday')
    tues = BooleanField('Tuesday')
    wed = BooleanField('Wednesday')
    thurs = BooleanField('Thursday')
    fri = BooleanField('Friday')
    sat = BooleanField('Saturday')
    sun = BooleanField('Sunday')
    startTime = DateTimeField('Start time (00:00-23:59)?',format='%H:%M', default= dt.datetime.now())
    endTime = DateTimeField('Start time (00:00-23:59)?',format='%H:%M', default= dt.datetime.now() + dt.timedelta(hours=1))
    submit = SubmitField("Add")

class StudentForm(Form):
    fullname = StringField('Name', validators=[Required(message="Name is required"),Length(0,64)])
    school  = SelectField(u'School', default='none', choices=[('none', 'Please select your school'), ('colm', 'Columbia University'), ('nyu', 'New York University')
        , ('other', 'Other')])
    grade = SelectField(u'Year', default='none', choices=[('none', 'Please select your year'), ('freshman', 'Freshman'), ('sophmore', 'Sophmore'), ('junior','Junior',),('senior','Senior'),('grad','Grad Student')
        , ('other', 'Other')])
    phonenumber = StringField('Phone Number', validators=[validatePhone])
    major = StringField('Major')
    submit = SubmitField()

class TutorForm(Form):
    fullname = StringField('Full Name', validators=[Required(message="Name is required"), Length(0, 64)])
    school  = SelectField(u'School', default='none', choices=[('none', 'Please select your school'), ('colm', 'Columbia University'), ('fordham', 'Fordham University'), ('hunter', 'Hunter University'), ('nyu', 'New York University'), ('pace', 'Pace University'), ('cunyq', 'Queens College, CUNY')
        , ('other', 'Other')])
    grade = SelectField(u'Grade', default = 'none', choices=[('none', 'Please select your grade'),('freshman', 'Freshman'), ('sophmore', 'Sophmore'), ('junior', 'Junior'),('senior', 'Senior'),
        ('grad', 'Masters'),('phd', 'Ph.D'),('alum', 'Alumni')])
    major = StringField('Major',validators=[Length(0, 64)])
    gpa = DecimalField("Bachelor's GPA", validators=[NumberRange(min=0,max=4,message="Please enter a value between 0.0 and 4.0"), Optional()])
    phonenumber = StringField('Phone', validators=[validatePhone])
    relexp = TextAreaField('Relevant Experience',validators=[Length(0,500)])
    submit = SubmitField()