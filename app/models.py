from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

class User(UserMixin,db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))
	username = db.Column(db.String(64), unique=True, index=True)
	created_on = db.Column(db.DateTime, default=db.func.now())
	updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
	student = db.relationship('Student',backref='user',lazy='dynamic')
	tutor = db.relationship('Tutor',backref='user',lazy='dynamic')

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class SignUp(db.Model):
	__tablename__  = 'signup'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True, index=True)
	created_on = db.Column(db.DateTime, default=db.func.now())

class Tutor(db.Model):
	__tablename__ = 'tutor'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	fullname = db.Column(db.String(64))
	school = db.Column(db.String(64))
	grade = db.Column(db.String(64))
	major = db.Column(db.String(64))
	gpa = db.Column(db.Float)
	phonenumber = db.Column(db.String(10))
	relexp = db.Column(db.String(500))
	created_on = db.Column(db.DateTime, default=db.func.now())
	updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

class Student(db.Model):
	__tablename__ = 'student'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	fullname = db.Column(db.String(64))
	school = db.Column(db.String(64))
	grade = db.Column(db.String(64))
	phonenumber = db.Column(db.String(10))
	major = db.Column(db.String(64))
	gethelp = db.relationship('GetHelp',backref='student',lazy='dynamic')

class GetHelp(db.Model):
	__tablename__ = 'get_help'
	id = db.Column(db.Integer, primary_key=True)
	student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
	class_number = db.Column(db.String(64))
	location = db.Column(db.String(64))
	help_comment = db.Column(db.String(64))
	duration = db.Column(db.String(64))
	start_time = db.Column(db.DateTime)
	created_on = db.Column(db.DateTime, default=db.func.now())

class Schedule(db.Model):
	__tablename__ = 'schedule'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	start = db.Column(db.DateTime)
	end = db.Column(db.DateTime)