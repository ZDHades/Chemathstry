from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm

# Form for getting Mass Fractions of a reaction
class mass_fraction(FlaskForm):
    reactants = StringField()
    products = StringField
    submit = SubmitField("Submit Query")