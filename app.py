from flask import Flask, render_template
from flask import jsonify
import numpy as np
import pandas as pd
import requests
import json
import ssl
from freshdesk.api import API
# multiple linear reg
api_key = "1ocb2Ebhrq5CAQVMKGBp"
domain = "pbltd"
password = "12345@abcde"

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('home.html')

@app.route('/Customer_Support')
def Customer_Support():
	headers = { 'Content-Type' : 'application/json' }

	ticket = {
	    'subject' : 'First',
	    'description' : 'Ticket detail',
	    'email' : 'abid@example.com',
	    'priority' : 1,
	    'status' : 2,
	    'cc_emails' : ['sample_email@domain.com', 'user_email@domain.com']
	}

	
	# print (r)
	# if r.status_code == 201:
	# 	print ("Ticket created successfully, the response is given below" + str(r.content))
	# 	print ("Location Header : " + str(r.headers['Location']))
	# else:
	# 	print ("Failed to create ticket, errors are displayed below,")
	# 	response = json.loads(r.content)
	# 	print (response["errors"])

	# 	print ("x-request-id : " + r.headers['x-request-id'])
	# 	print ("Status Code : " + str(r.status_code))
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
	app.run(debug=True)