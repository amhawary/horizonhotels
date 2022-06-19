from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, PasswordField, SelectField, BooleanField, SubmitField


class loginform(FlaskForm):
    useremail = EmailField('Enter e-mail')
    pw = PasswordField('Enter password')
    submit = SubmitField()

    
    
