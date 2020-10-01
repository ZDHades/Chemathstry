from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Email, EqualTo, email_validator, DataRequired
from flask_wtf import FlaskForm

# form for the register page
class Register(FlaskForm):
    first_name = StringField()
    last_name = StringField()
    email = StringField(validators=[Email(message='Not a valid email address')])
    password = PasswordField()
    confirm_password = PasswordField(EqualTo('password'))
    accept_tos = BooleanField('I accept the TOS', validators=[DataRequired()])
    submit = SubmitField('Submit')

# form for login page
class Login(FlaskForm):
    email = StringField(validators=[Email(message='Not a valid email address')])
    password = PasswordField()
    submit = SubmitField('Submit')

# form for the settings page
class Settings(FlaskForm):
    first_name = StringField()
    last_name = StringField()
    email = StringField(validators=[Email(message='Not a valid email address')])
    password = PasswordField()
    confirm_password = PasswordField(EqualTo('password'))
    submit = SubmitField('Submit')
