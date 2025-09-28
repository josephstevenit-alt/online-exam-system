from .extensions import db
from datetime import datetime
from sqlalchemy.dialects.mysql import JSON

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, pwd):
        from .extensions import bcrypt
        self.password_hash = bcrypt.generate_password_hash(pwd).decode('utf-8')

    def check_password(self, pwd):
        from .extensions import bcrypt
        return bcrypt.check_password_hash(self.password_hash, pwd)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stem = db.Column(db.Text, nullable=False)
    options = db.Column(JSON, nullable=False)   # list of options
    correct_index = db.Column(db.Integer, nullable=False)
    mark = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ExamResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Float, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    details = db.Column(JSON)
    taken_at = db.Column(db.DateTime, default=datetime.utcnow)
    user = db.relationship('User', backref='results')
