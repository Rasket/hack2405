from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from base64 import b64encode


class User(UserMixin, db.Model):
	"""docstring for User"""
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), index = True, unique = True)
	email = db.Column(db.String(120), index = True, unique = True)
	password_hash = db.Column(db.String(128))
	avatar = db.Column(db.LargeBinary)
	about_me = db.Column(db.String(140))
	last_seen = db.Column(db.DateTime, default=datetime.utcnow)
	followed = db.relationship(
		'User', secondary = followers,
		primaryjoin = (followers.c.follower_id == id),
		secondaryjoin = (followers.c.followed_id == id),
		backref = db.backref('followers', lazy = 'dynamic'), lazy = 'dynamic'
		)
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
