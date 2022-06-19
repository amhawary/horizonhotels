from optparse import check_builtin
from tkinter.tix import Select
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, PasswordField, SelectField, BooleanField, SubmitField, TelField
from wtforms.validators import EqualTo, Length, DataRequired, Optional, ValidationError

class accountform(FlaskForm):
    fullname = StringField('Enter full name:',validators = [DataRequired(message='Name cannot be empty'),Length(min=1,max=100)])
    title = SelectField('Enter preferred name(s):',validators = [DataRequired()],choices=[('Mr','Mr'),('Mrs','Mrs'),('Ms','Ms'),('Mx','Mx'),('Dr','Dr')])
    prefname = StringField('',validators=[DataRequired(message='Name cannot be empty'),Length(min=1,max=20)])
    useremail = EmailField('Enter email',validators=[DataRequired(message='Email cannot empty'),Length(min=10,max=60)])
    confirmmail = EmailField('Re-enter email',validators=[DataRequired(message='Please confirm email'), EqualTo(useremail)])
    pw = PasswordField('Enter password',validators=[DataRequired(message='Password cannot empty'),Length(min=8,max=30)])
    confirmpw = PasswordField('Re-enter password',validators=[DataRequired(message='Please confirm password'), EqualTo(pw)])
    phone = TelField('Enter phone number (Optional)',validators= [Optional()])
    currency = SelectField()
    page = IntegerField()
    cancel = IntegerField()
    refund = IntegerField()
    bookingref = IntegerField()