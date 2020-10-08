from app import db, login
from datetime import datetime
from flask_login import UserMixin
from app.blueprints.authentication.models import User

# DB table for saving Molar Mass Queries by user_id
class MMQueries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    q_MM = db.Column(db.String)
    s_MM = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.ForeignKey('user.id'))

    def to_dict(self):
        data = {
            'user_id' : self.user_id,
            'q_MM' : self.q_MM,
            's_MM' : self.s_MM,
            'created_on' : self.created_on
        }
        return data
    
    def __repr__(self):
        return f'{self.s_MM} = {self.q_MM}'