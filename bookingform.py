from optparse import check_builtin
from tkinter.tix import Select
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, PasswordField, SelectField, BooleanField, StringField, FloatField


class bookingform(FlaskForm):
    city = SelectField()
    checkIn = StringField()
    checkOut = StringField()
    roomType = SelectField() 
    guests = IntegerField()
    paid = BooleanField()
    bookingDate = StringField()
    price = FloatField()
    guestName = StringField()
    userNotes = StringField()
    checkindate = StringField()
    checkoutdate = StringField()

class bookingform2(FlaskForm):
    city = SelectField()
    checkIn = StringField()
    checkOut = StringField()
    roomType = SelectField() 
    guests = IntegerField()
    paid = BooleanField()
    bookingDate = StringField()
    price = IntegerField()
    guestName = StringField()
    userNotes = StringField()
    checkindate = StringField()
    checkoutdate = StringField()