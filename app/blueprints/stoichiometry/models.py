from app import db, login
from datetime import datetime
from flask_login import UserMixin
from app.blueprints.authentication.models import User

# db table for saving stoich queries by user_id
class StoichQueries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    q_reactants = db.Column(db.String)
    q_products = db.Column(db.String)
    s_reactants = db.Column(db.String)
    s_products = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.ForeignKey('user.id'))

    # create a method that will allow for display via api
    def to_dict(self):
        data = {
            'user_id' : self.user_id,
            'q_reactants' : self.q_reactants,
            'q_products' : self.q_products,
            's_reactants' : self.s_reactants,
            's_products' : self.s_products,
            'created_on' : self.created_on
        }
        return data

    def my_queries(self):
        my_queries = self.query.filter_by(user_id=self.user_id)
        return my_queries

    def __repr__(self):
        return f'Solution: {self.s_reactants} = {self.s_products}' 
