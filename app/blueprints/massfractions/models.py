from app import db
from datetime import datetime
from app.blueprints.authentication.models import User

# DB table for saving Mass Fraction Queries by User_ID
class MFQueries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    q_reactants = db.Column(db.String)
    q_products = db.Column(db.String)
    solution = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.ForeignKey('user.id'))

    # create a method that will allow for display via api
    def to_dict(self):
        data = {
            'user_id' : self.user_id,
            'q_reactants' : self.q_reactants,
            'q_products' : self.q_products,
            'solution' : self.solution,
            'created_on' : self.created_on
        }
        return data
    
    def __repr__(self):
        return f'solution: {self.s_reactants} = {self.s_products}'