from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from base64 import b64encode
from flask_login import UserMixin
from app import login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
	"""docstring for User"""
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), index = True, unique = True)
	email = db.Column(db.String(120), index = True, unique = True)
	password_hash = db.Column(db.String(128))
	avatar = db.Column(db.LargeBinary)
	about_me = db.Column(db.String(500))
	ecological = db.Column(db.Integer)
	public = db.Column(db.Boolean, default=True)
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
	def get_avatar(self):
		try:
			return b64encode(self.avatar).decode('ascii')
		except TypeError:
			return None				
	def __repr__(self):
		return f'<User {self.username}>'
