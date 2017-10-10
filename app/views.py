from flask import (Flask, request, render_template)
from app import app
from datetime import datetime

def convert_name(firstname,lastname,gender):
    if gender.lower() == "m":
        return "Mr. " + firstname.capitalize() + " " + lastname.capitalize()
    elif gender.lower() == "f":
        return "Ms. " + firstname.capitalize() + " " + lastname.capitalize()
    else:
        return "Mx. " + firstname.capitalize() + " " + lastname.capitalize()

def math_computation(num1,num2,operator):
    if operator.lower() == "subtract":
        return int(num1) - int(num2)
    elif operator.lower() == "add":
        return int(num1) + int(num2)
    elif operator.lower() == "multiply":
        return int(num1)*int(num2)
    elif operator.lower() == "divide":
        return float(num1)/float(num2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compute', methods=['GET','POST'])
def compute():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operator = request.form['operator']
    answer = math_computation(num1,num2,operator)
    return render_template('compute.html', answer=answer)

@app.route('/hello', methods=['GET','POST'])
def hello():
    if request.form['firstname']:
        firstname = request.form['firstname']
    else:
        firstname = request.args.get('firstname')
    if request.form['lastname']:
        lastname = request.form['lastname']
    else:
        lastname = request.args.get('lastname')
    if request.form['gender']:
        gender = request.form['gender']
    else:
        gender = request.args.get('gender')
    # firstname = request.form['firstname'] and request.args.get('firstname')
    # lastname = request.form['lastname'] and request.args.get('lastname')
    # gender = request.form['gender'] and request.args.get('gender')
    name = convert_name(firstname,lastname,gender)
    return render_template('hello.html', name=name)
# def hello(firstname,lastname,gender):


@app.route('/date', methods=['GET','POST'])
def date():
    date_value = datetime.now().strftime('%Y-%m-%d')
    return render_template('date.html', date_value=date_value)
