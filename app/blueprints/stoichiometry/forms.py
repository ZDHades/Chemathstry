from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm

# form for stoichiometry
class two_part_reaction(FlaskForm):
    reactants = StringField()
    products = StringField()
    submit = SubmitField('Submit!')

    # placeholder for reactants = NH4ClO4, Al
    # placeholder for products = Al2O3, HCl, H2O, N2