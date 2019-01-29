from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import os, logging, psycopg2 
from datetime import datetime 
import ujson
import uuid
from flask_bootstrap import Bootstrap
from libs import postgres , utils , logs, rediscache, notification
from appsrc import app, logger
from flask import make_response
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 

class ReusableForm(Form):
    Firstname = TextField('Firstname:', validators=[validators.required()])
    Lastname = TextField('Lastname:', validators=[validators.required()])
    Email = TextField('Email:', validators=[validators.required()])
    Company = TextField('Company:', validators=[validators.required()])
    PhoneNumber = TextField('PhoneNumber:', validators=[validators.required()])
    Host = TextField('Host:', validators=[validators.required()])

           

@app.route('/guest', methods=['GET', 'POST'])
def guest():
    try:
        cookie, cookie_exists =  utils.getCookie()
        logger.debug(utils.get_debug_all(request))

        form = ReusableForm(request.form)
        hosts = postgres.__getSFUsers()

        print(form.errors)
        if request.method == 'POST':
            Firstname=request.form['Firstname']
            Lastname=request.form['Lastname']
            Email=request.form['Email']
            Company=request.form['Company']
            PhoneNumber=request.form['PhoneNumber']
            Host=request.form['Host']
            postgres.__saveGuestEntry(Firstname, Lastname, Email, Company, PhoneNumber, Host)
            data = render_template('guest.html', form=form, hosts=hosts['data'], registered=True)

            return utils.returnResponse(data, 200, cookie, cookie_exists)
        
        print(form)
        if form.validate():
            # Save the comment here.
            flash('Hello ' + Firstname)
        else:
            flash('All the form fields are required. ')
        
        # gets the user
        
        data = render_template('guest.html', form=form, hosts=hosts['data'])
        
        return utils.returnResponse(data, 200, cookie, cookie_exists)
    except Exception as e:
        import traceback
        traceback.print_exc()
        cookie, cookie_exists =  utils.getCookie()
        return utils.returnResponse("An error occured, check logDNA for more information", 200, cookie, cookie_exists)

        