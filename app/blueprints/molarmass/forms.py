from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm

# Single field form for Molar Mass
class MolarMass(FlaskForm):
    get_MM = StringField()
    submit = SubmitField("Submit Query")
    