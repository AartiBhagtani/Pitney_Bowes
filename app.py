from flask import Flask, render_template, flash, redirect, url_for, request
from flask import jsonify
import numpy as np
import pandas as pd
import requests
import json
import ssl
from freshdesk.api import API
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

# multiple linear reg
api_key = "1ocb2Ebhrq5CAQVMKGBp"
domain = "pbltd"
password = "zzzz"

app = Flask(__name__)

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    contact = StringField('Contact', [validators.Length(min=8, max=10)])
    query = StringField('Query', [validators.Length(min=1, max=500)])

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/Customer_Support', methods=['GET', 'POST'])
def Customer_Support():
	
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		name = form.name.data
		email = form.email.data
		contact = form.contact.data
		query = form.query.data
		headers = { 'Content-Type' : 'application/json' }

		ticket = {
			'subject' : name+' '+contact,
			'description' : query,
			'email' : email,
			'priority' : 1,
			'status' : 2,
			'cc_emails' : ['sample_email@domain.com', 'user_email@domain.com']
		}
		r = requests.post("https://"+ domain +".freshdesk.com/api/v2/tickets", auth = (api_key, password), headers = headers, data = json.dumps(ticket))
		if r.status_code == 201:
			print ("Ticket created successfully, the response is given below" + str(r.content))
			
			flash('Ticket created successfully.', 'success')
			print ("Location Header : " + str(r.headers['Location']))
			return redirect(url_for('Customer_Support'))
		else:
			flash('Ticket cannot be created ','danger')
			# print ("Failed to create ticket, errors are displayed below,")
			# response = json.loads(r.content)
			# print (response["errors"])
			# print ("x-request-id : " + r.headers['x-request-id'])
			# print ("Status Code : " + str(r.status_code))
		# flash('Your Query is sent and ticket is generated', 'success')
	return render_template('Customer_Support.html', form=form)
	
	return render_template('Customer_Support.html')

@app.route('/Returns_Management')
def Returns_Management():
	return render_template('Returns_Management.html')

@app.route('/Order_Management')
def Order_Management():
	return render_template('Order_Management.html')

@app.route('/Marketing')
def Marketing():
	return render_template('Marketing.html')	

@app.route('/HDM')
def HDM():
	return render_template('HDM.html')	

if __name__ == '__main__':
	app.secret_key='secret123'
	app.run(debug=True)
	