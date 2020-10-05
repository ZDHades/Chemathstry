from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# the user table
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    stoich_queries = db.relationship('StoichQueries', backref='user', lazy=True)

    # method to secure password
    def hash_pass(self, original_password):
        self.password = generate_password_hash(original_password)

    # method to verify password against databases secure password
    def check_password(self, original_password):
        return check_password_hash(self.password, original_password)

    def __repr__(self):
        return f"<user: {self.email}>"

    # def my_queries(self):
    #     return self.my_queries

@login.user_loader
def login_user(id):
    return User.query.get(int(id))
