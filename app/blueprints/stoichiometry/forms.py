from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm

# form for stoichiometry
class two_part_reaction(FlaskForm):
    reactants = StringField()
    products = StringField()
    submit = SubmitField('Submit Query')
