from flask import (Flask, request, jsonify)
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
    if operator == "subtract":
        return int(num1) - int(num2)
    elif operator == "add":
        return int(num1) + int(num2)
    elif operator == "multiply":
        return int(num1)*int(num2)
    elif operator == "divide":
        return float(num1)/float(num2)

@app.route('/compute', methods=['GET','POST'])
def compute():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    operator = request.args.get('operator')
    answer = math_computation(num1,num2,operator)
    return jsonify(answer)

@app.route('/hello', methods=['GET','POST'])
def hello():
    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')
    gender = request.args.get('gender')
    name = convert_name(firstname,lastname,gender)
    return jsonify(name)

@app.route('/date', methods=['GET','POST'])
def date():
    date_value = datetime.now().strftime('%Y-%m-%d')
    return jsonify(date_value)
