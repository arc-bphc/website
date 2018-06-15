from app import db

class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	email = db.Column(db.String(50), unique=True)
	name = db.Column(db.String(64), unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	contact_no = db.Column(db.String(10),unique=True)
	isAdmin = db.Column(db.String(1))
	fb = db.Column(db.String(100),unique=True)
	github = db.Column(db.String(100),unique=True)
	linkedin = db.Column(db.String(100),unique=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return '<User {}>'.format(self.id)

class BlogPost(db.Model):
	post_id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(50))
	tags = db.Column(db.String(50))

	def __repr__(self):
		return '<User {}>'.format(self.post_id)
class user_posts(db.Model):
	link_id = db.Column(db.Integer,primary_key=True)
	user_id = db.Column(db.Integer)
	post_id = db.Column(db.Integer)

