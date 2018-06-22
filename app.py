from flask import Flask, render_template
from flask import jsonify
import numpy as np
import pandas as pd
# multiple linear reg

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('home.html')

@app.route('/Customer_Support')
def Customer_Support():
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