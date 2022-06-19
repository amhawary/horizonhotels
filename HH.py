
from array import typecodes
from ast import Return
from random import random
from flask import Flask, redirect, render_template, request, session, flash, url_for
from flask_login import login_required,login_user, logout_user, current_user
import mysql.connector
from mysql.connector import errorcode
from datetime import date, time, timedelta, datetime
from mysqlx import Session
import signupform, loginform, dbfunc, bookingform, accountpage
from passlib.hash import sha256_crypt

bookingRedirect = [False]
app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

conn = dbfunc.get_connection()


dbcursor = conn.cursor()
dbcursor.execute('UPDATE reservations SET Ongoing = 0 WHERE %s > CheckOut',(date.today(),))
conn.commit()
@app.route('/',methods = ["GET","POST"])
@app.route('/index')
def index():
    if 'currency' not in session:
        session['currency'] = 'GBP'
    paid = False
    if request.method == "POST":
        conn = dbfunc.get_connection()
        if conn != None:
                    dbcursor = conn.cursor()
                    add_booking = ("INSERT INTO reservations (ROOMNUM, USER, HOTEL, ROOMTYPE, CheckIn, CheckOut, Guests, BookingDate, Price, Ongoing) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 1)")
                    data_booking = (session["room"][0],session["email"],session["choices"][0],session["choices"][1],session["choices"][2],session["choices"][3],session["choices"][4],session["choices"][5],session["choices"][6],)
                    dbcursor.execute(add_booking,data_booking)
                    conn.commit()
                    paid = True
    bookingRedirect[0] = False
    conn = dbfunc.get_connection()
    if conn != None:
        dbcursor = conn.cursor()
        dbcursor.execute('SELECT city, hid, pricePeak, priceOff, region, hname, hotelDesc, feat FROM HOTELS WHERE Feat = 1;')
        hotels = dbcursor.fetchall()
        ranges ={}
        for hotel in hotels:
            min = hotel[3]
            upper = hotel[2] * 1.5
            if session.get('currency') == 'USD':
                min = min * 1.6
                upper = upper * 1.6
            elif session.get('currency') == 'EUR':
                min = min * 1.2
                upper = upper * 1.2               
            txt = (str(min) + " - " + str(upper) + " " + session.get('currency'))
            ranges[hotel[0]] = txt
        return render_template('HH.html', paid = paid, ranges = ranges, hotels = hotels)

    return 0   

@app.route('/explore')
def explore():
    if 'currency' not in session:
        session['currency'] = 'GBP'
    bookingRedirect[0] = False
    conn = dbfunc.get_connection()
    if conn != None:
        dbcursor = conn.cursor()
        dbcursor.execute('SELECT city, hid, pricePeak, priceOff, region, hname, hotelDesc, feat  FROM HOTELS;')
        hotels = dbcursor.fetchall()
        ranges = {}

        dbcursor.execute('SELECT type, roomDesc, guests FROM room_types;')
        types = dbcursor.fetchall()
        rtypes = {}

        for hotel in hotels:
            min = hotel[3]
            upper = hotel[2] * 1.5
            if session.get('currency') == 'USD':
                    min = min * 1.6
                    upper = upper * 1.6
            elif session.get('currency') == 'EUR':
                    min = min * 1.2
                    upper = upper * 1.2               
            txt = (str(min) + " - " + str(upper) + " " + session.get('currency'))
            ranges[hotel[0]] = txt
        
        for type in types:
            rtypes[type[0]] = "r" + type[0]

        return render_template('HHexplore.html', hotels = hotels, types = types, rtypes = rtypes, ranges = ranges)
    return 0

@app.route('/about')
def about():
    bookingRedirect[0] = False
    return render_template('HHabout.html')

@app.route('/admin')
def admin():
    if session.get('admin') == 1:
        return render_template('HHadmin.html')
    else: return redirect('/')

@app.route('/booking',methods = ["GET","POST"])
def booking():
    found = 0
    error = []
    form = bookingform.bookingform()
    paid = int(form.paid.data)
    if request.method == "POST":
        pass
    if 'email' in session:
                bookingRedirect[0] = False
                conn = dbfunc.get_connection()
                if conn != None:
                    dbcursor = conn.cursor()
                    dbcursor.execute('SELECT City,PricePeak,PriceOff,HID FROM HOTELS;')
                    cities = dbcursor.fetchall()
                    dbcursor.execute('SELECT TYPE,Guests,RATE,GuestCharge FROM ROOM_TYPES;')
                    roomtypes = dbcursor.fetchall()
                    dbcursor.execute('SELECT days, pname, diff FROM policy WHERE pname = "Advance" ORDER BY days DESC;')
                    advancetable = dbcursor.fetchall()
                    types={}
                    rates = {}
                    extra = {}
                    for room in roomtypes:
                        types[room[0]]=room[1]
                        rates[room[0]]=room[2]
                        extra[room[0]]=room[3]
                    offSzn = {}
                    peakSzn = {}
                    for city in cities:
                        offSzn[city[3]]=city[2]
                        peakSzn[city[3]]=city[1]
                    advance = {}
                    for advancerow in advancetable:
                        advance[advancerow[0]] = advancerow[2]
                    prices = [offSzn,peakSzn,rates,advance,extra]
                    userCity = form.city.data
                    userRType = form.roomType.data
                    if (userCity):
                            if(userRType):
                                data = [form.checkIn.data, form.checkIn.data, form.checkOut.data, userCity, userRType]
                                dbcursor.execute("SELECT r.RoomNum, r.Hotel, r.ROOMTYPE FROM rooms r LEFT JOIN reservations re ON r.hotel = re.HOTEL AND r.RoomType = re.ROOMTYPE AND (%s NOT BETWEEN re.CheckIn AND re.CheckOut) AND (re.CheckIn NOT BETWEEN %s AND %s) WHERE r.hotel = %s AND r.RoomType = %s",data)
                                availablerooms = dbcursor.fetchall()
                                choices = [userCity,userRType,form.checkIn.data,form.checkOut.data,form.guests.data,form.bookingDate.data,form.price.data]
                                session['choices'] = choices
                                if dbcursor.rowcount > 0:
                                    print("Row Count =", dbcursor.rowcount)
                                    session["room"] = availablerooms[0]
                                    dbcursor.execute("SELECT MAX(BookingRef) FROM reservations")
                                    session["bookingref"] = dbcursor.fetchone()[0]
                                    found = True

                                else:
                                    error.append ("No available rooms at the moment, sorry about that.")
                    return render_template('HHbooking.html', form = form, cities = cities, types = types, roomtypes = roomtypes, prices = prices, found = found, advance = advance)
                return render_template('HHbooking.html',form = form, cities = cities, types = types, roomtypes = roomtypes, prices = prices, found = found, advance = advance)
    else: 
        bookingRedirect[0] = True
        return redirect('/login')
                        
@app.route('/account', methods = ["GET","POST"])
def account():
        form = accountpage.accountform()
        if 'email' in session:
                    conn = dbfunc.get_connection()
                    if conn != None:
                        cancelled = []
                        error = []
                        if (form.page.data):
                            page = form.page.data
                        else: page = 1
                        dbcursor = conn.cursor()
                        dbcursor.execute('SELECT hid, city FROM hotels')
                        hotels = dbcursor.fetchall()
                        cities = {}
                        for city in hotels:
                            cities[city[0]]=city[1]
                        dbcursor.execute('SELECT * FROM accounts WHERE email = %s;',(session["email"],))
                        user = dbcursor.fetchone()
                        dbcursor.execute('SELECT * FROM reservations WHERE user = %s AND ongoing = 1;',(session["email"],))
                        ongoing = dbcursor.fetchall()
                        current = []
                        for res in ongoing:
                            reserv = list(res)
                            reserv[6] = cities[res[6]]
                            if res[2] > date.today():
                                reserv.append('Booked')
                            else: 
                                reserv.append('Active')
                            current.append(reserv)
                        dbcursor.execute('SELECT * FROM reservations WHERE user = %s AND ongoing = 0;',(session["email"],))
                        ended = dbcursor.fetchall()
                        past = []
                        for res in ended:
                            reserv = list(res)
                            reserv[6] = cities[res[6]]
                            if res[11]:
                                reserv.append('Cancelled, fee = ' + res[11])
                            else: reserv.append('Completed')
                            past.append(reserv)
                        if page == 2:
                            hashedpw = sha256_crypt.hash(form.pw.data)
                            checkEmailTaken = "SELECT * FROM accounts WHERE email = %s;"
                            email = [form.useremail.data]
                            dbcursor.execute(checkEmailTaken,email)
                            rows = dbcursor.fetchall()           
                            if dbcursor.rowcount > 0:
                                    error.append("Email already taken, please choose another")   
                            else:          
                                add_accounts = ("INSERT INTO accounts "
                                "(email, phonenum, title, fullName, prefName, admin, passwrd, currency)"
                                "VALUES (%s, %s, %s, %s, %s,0,%s,%s)")
                                data_accounts = (form.useremail.data, form.phone.data,form.title.data,form.fullname.data,form.prefname.data,hashedpw, form.currency.data,)
                                dbcursor.execute(add_accounts,data_accounts)
                                conn.commit()
                                return redirect('/login')
                        elif page == 3:
                            dbcursor.execute('SELECT * FROM RESERVATIONS WHERE BookingRef = %s', (form.cancel.data,))
                            cancel = dbcursor.fetchone()
                            cancelled = list(cancel)
                            dbcursor.execute('SELECT * FROM policy WHERE pname = "Cancel"')
                            diff = dbcursor.fetchall()
                            daydiff = cancel[2] - date.today()
                            cancelled[11] = 0
                            for dif in diff:
                                if int(daydiff.days) > dif[0]:
                                        cancelled[11] = dif[2] * cancelled[8]
                        elif page == 4:
                              page = 1
                              print(form.refund.data)
                              dbcursor.execute('UPDATE reservations SET Ongoing = 0 AND cancelFee = %s WHERE bookingRef = %s',(form.refund.data,form.bookingref.data)) # set cancelFee to %s
                              conn.commit()
                        elif page == 5:
                            dbcursor.execute('DELETE FROM accounts WHERE email = %s',(session["email"],))
                            conn.commit()
                            return redirect(url_for("logout"))
                        return render_template('HHaccount.html', page = page, user = user, current = current, past = past, cancelled = cancelled)
        else: 
                        return redirect('/login')

@app.route('/login',methods = ["GET","POST"])
def login():
    error = []
    if bookingRedirect[0] == True:
                    error.append("You must be logged in to start booking")
    conn = dbfunc.get_connection()
    form = loginform.loginform()
    if 'email' in session:
            return redirect('/')
    else:
        if(request.method == "POST"):
            if conn != None:
                dbcursor = conn.cursor()
                pw =  form.pw.data
                getHash = "SELECT passwrd FROM accounts WHERE email = %s;"
                email = [form.useremail.data]
                dbcursor.execute(getHash,email)
                row = dbcursor.fetchone()
                if dbcursor.rowcount > 0:
                        if sha256_crypt.verify( pw,row[0]):
                            session["email"] = form.useremail.data
                            dbcursor.execute("SELECT admin, currency FROM accounts WHERE email = %s;",email)
                            x = str(dbcursor.fetchone())
                            if "1" in x:
                                session["admin"] = 1
                            else:
                                session["admin"] = 0
                            if 'USD' in x:
                                session["currency"] = 'USD'
                            elif 'EUR'in x:
                                session["currency"] = 'EUR'
                            else: session["currency"] = 'GBP'
                            if bookingRedirect[0] == True:
                                return redirect('/booking')
                            else: return redirect('/')
                        else:
                            error.append("Email or Password is incorrect")
                else: 
                                error.append("Email or Password is incorrect")
        return render_template('HHlogin.html', form = form, error = error )

@app.route('/logout', methods = ["GET","POST"])
def logout():
    try:
            session.pop("email", None)
            session.pop("admin", None)
            return redirect('/')
    except:
        return redirect('/')

@app.route('/signup',methods = ["GET","POST"])
def signup():
    if 'email' in session:
        return redirect('/')
    else: 
        error = []
        conn = dbfunc.get_connection()
        form = signupform.signupform()
        if request.method=="POST":
            if conn != None:
                dbcursor = conn.cursor()
                hashedpw = sha256_crypt.hash(form.pw.data)
                checkEmailTaken = "SELECT * FROM accounts WHERE email = %s;"
                email = [form.useremail.data]
                dbcursor.execute(checkEmailTaken,email)
                rows = dbcursor.fetchall()           
                if dbcursor.rowcount > 0:
                            error.append("Email already taken, please choose another")   
                else:          
                    add_accounts = ("INSERT INTO accounts "
                    "(email, phonenum, title, fullName, prefName, admin, passwrd, currency)"
                    "VALUES (%s, %s, %s, %s, %s,0,%s,%s)")
                    data_accounts = (form.useremail.data, form.phone.data,form.title.data,form.fullname.data,form.prefname.data,hashedpw, form.currency.data,)
                    dbcursor.execute(add_accounts,data_accounts)
                    conn.commit()
                    return redirect('/login')
    return render_template('HHsignup.html', form = form, error = error)
app.run(debug = True)