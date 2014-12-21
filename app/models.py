from . import db

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))

class Tutor(db.Model):
	__tablename__ = 'tutor'
	id = db.Column(db.Integer, primary_key=True)
	fullname = db.Column(db.String(64))
	email = db.Column(db.String(64), unique=True, index=True)
	school = db.Column(db.String(64))
	grade = db.Column(db.String(64))
	major = db.Column(db.String(64))
	gpa = db.Column(db.Float)
	phonenumber = db.Column(db.String(10))
	relexp = db.Column(db.String(500))
	created_on = db.Column(db.DateTime, default=db.func.now())
	updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())