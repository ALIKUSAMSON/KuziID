from sqlalchemy.orm import relationship
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from run import *
from forms import *

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password = db.Column(db.String(120), index=True,)

	def is_authenticated(self):
		return True
 
 	def is_active(self):
 		return True
 
 	def is_anonymous(self):
 		return False
 
 	def get_id(self):
 		return unicode(self.id)
 
 	def __repr__(self):
 		return '<User %r>' % (self.username)


class Excelpost(db.Model):
    __tablename__ = 'excels'
    id = db.Column(db.Integer, primary_key=True)
    subcounty = db.Column(db.String(255),index=True,unique=True)
    parish = db.Column(db.String(255),index=True,unique=True)
    village = db.Column(db.String(255),index=True)



class Leader(db.Model):

	__tablename__ = 'leaders'
	id = db.Column(db.Integer, primary_key=True)
	category = db.Column(db.String(255), index=True)
	name = db.Column(db.String(255),index=True)
	email = db.Column(db.String(255),index=True,unique=True)
	position = db.Column(db.String(255),index=True)
	year = db.Column(db.Date,index=True)
	contact = db.Column(db.String(255),index=True,unique=True)

class Import( db.Model):
	__tablename__ = 'import'
	id = db.Column(db.Integer, primary_key=True)
	importname = db.Column(db.String(255),index=True)

class LC5(db.Model):
	__tablename__ = 'lc5'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255),index=True)
	email = db.Column(db.String(255),index=True,unique=True)
	position = db.Column(db.String(255),index=True)
	year = db.Column(db.String(255),index=True)
	contact = db.Column(db.String(255),index=True,unique=True)


class WomanMP(db.Model):
	__tablename__ = 'Womanmp'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255),index=True)
	email = db.Column(db.String(255),index=True,unique=True)
	position = db.Column(db.String(255),index=True)
	year = db.Column(db.String(255),index=True)
	contact = db.Column(db.String(255),index=True,unique=True)


class WomanCounsellor(db.Model):
	__tablename__ = 'womanc'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255),index=True)
	email = db.Column(db.String(255),index=True,unique=True)
	position = db.Column(db.String(255),index=True)
	year = db.Column(db.Integer,index=True)
	contact = db.Column(db.Integer,index=True,unique=True)

class NRM(db.Model):
	__tablename__ = 'nrm'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255),index=True)
	email = db.Column(db.String(255),index=True,unique=True)
	position = db.Column(db.String(255),index=True)
	year = db.Column(db.Integer,index=True)
	contact = db.Column(db.Integer,index=True,unique=True)

class Special(db.Model):
	__tablename__ = 'special'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255),index=True)
	email = db.Column(db.String(255),index=True,unique=True)
	position = db.Column(db.String(255),index=True)
	year = db.Column(db.Integer,index=True)
	contact = db.Column(db.Integer,index=True,unique=True)

class ER(db.Model):
	__tablename__ = 'er'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255),index=True)
	email = db.Column(db.String(255),index=True,unique=True)
	position = db.Column(db.String(255),index=True)
	year = db.Column(db.Integer,index=True)
	contact = db.Column(db.Integer,index=True,unique=True)

class ARMY(db.Model):
	__tablename__ = 'army'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255),index=True)
	email = db.Column(db.String(255),index=True,unique=True)
	position = db.Column(db.String(255),index=True)
	year = db.Column(db.Integer,index=True)
	contact = db.Column(db.Integer,index=True,unique=True)

class Constituency(db.Model):
	__tablename__ = 'constituency'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255),index=True)
	email = db.Column(db.String(255),index=True,unique=True)
	position = db.Column(db.String(255),index=True)
	year = db.Column(db.Integer,index=True)
	contact = db.Column(db.Integer,index=True,unique=True)

class Ledge(db.Model):
	__tablename__ = 'ledges'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255),index=True)
	email = db.Column(db.String(255),index=True,unique=True)
	position = db.Column(db.String(255),index=True)
	year = db.Column(db.Integer,index=True)
	contact = db.Column(db.Integer,index=True,unique=True)

class Other(db.Model):
	__tablename__ = 'other'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255),index=True,unique=True)
	email = db.Column(db.String(255),index=True,unique=True)
	position = db.Column(db.String(255),index=True)
	year = db.Column(db.Integer,index=True)
	contact = db.Column(db.Integer,index=True,unique=True)

class Options(db.Model):
	__tablename__ = 'selects'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255),index=True,unique=True)
	email = db.Column(db.String(255),index=True,unique=True)
	position = db.Column(db.String(255),index=True)
	year = db.Column(db.Integer,index=True)
	contact = db.Column(db.Integer,index=True,unique=True)

class Choice(db.Model):
	__tablename__ ="category"
	id = db.Column(db.Integer, primary_key=True)
	namecategory = db.Column (db.String(50))

	def __repr__(self):
		return '{}'.format(self.namecategory)

def choice_query():
	return Choice.query


