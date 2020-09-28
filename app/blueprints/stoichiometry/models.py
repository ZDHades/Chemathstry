from app import db, login
from datetime import datetime
from flask_login import UserMixin
from app.blueprints.authentication.models import User

# db table for saving stoich queries by user_id
class Stoich_queries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reactants = db.Column(db.String)
    products = db.Column(db.String)
    solution = db.Column(db.String)
    user_id = db.Column(db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<user: {self.user_id}> | <solution: {self.solution}>'
