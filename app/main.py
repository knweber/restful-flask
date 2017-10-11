from flask import (Flask, request, jsonify)
from app import app
from datetime import datetime

# Takes parameters from '/hello' query and constructs a full name
def convert_name(firstname,lastname,gender):
    if gender.lower() == "m": # male
        return "Mr. " + firstname.capitalize() + " " + lastname.capitalize()
    elif gender.lower() == "f": # female
        return "Ms. " + firstname.capitalize() + " " + lastname.capitalize()
    else: # gender-queer!
        return "Mx. " + firstname.capitalize() + " " + lastname.capitalize()

# Takes parameters from '/compute' query and runs the corresponding operation
def math_computation(num1,num2,operator):
    if operator == "subtract":
        return int(num1) - int(num2)
    elif operator == "add":
        return int(num1) + int(num2)
    elif operator == "multiply":
        return int(num1)*int(num2)
    elif operator == "divide":
        return float(num1)/float(num2)

@app.route('/')
def index():
    return jsonify("Kristianna Weber -- Pinterest Tech Challenge (Instructions located at https://github.com/knweber/restful-flask)")

@app.route('/compute')
def compute():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    operator = request.args.get('operator')
    # run operation with given parameters
    answer = math_computation(num1,num2,operator)
    return jsonify(answer)

@app.route('/hello')
def hello():
    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')
    gender = request.args.get('gender')
    # build full name from given parameters
    name = convert_name(firstname,lastname,gender)
    return jsonify(name)

@app.route('/date')
def date():
    # returns current date in the format YYYY-MM-DD
    date_value = datetime.now().strftime('%Y-%m-%d')
    return jsonify(date_value)
