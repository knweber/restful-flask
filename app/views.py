from flask import (Flask, request, render_template)
from app import app
from datetime import datetime

def convert_name(firstname,lastname,gender):
    if gender.lower() == "m":
        return "Mr. " + firstname.capitalize() + " " + lastname.capitalize()
    elif gender.lower() == "f":
        return "Ms. " + firstname.capitalize() + " " + lastname.capitalize()

def math_computation(num1,num2,operator):
    if operator.lower() == "subtract":
        return int(num1) - int(num2)
    elif operator.lower() == "add":
        return int(num1) + int(num2)
    elif operator.lower() == "multiply":
        return int(num1)*int(num2)
    elif operator.lower() == "divide":
        return int(num1)/int(num2)

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
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    gender = request.form['gender']
    name = convert_name(firstname,lastname,gender)
    return render_template('hello.html',name=name)

@app.route('/date', methods=['POST'])
def date():
    date_obj = {'today': datetime.now().strftime('%Y-%m-%d')}
    return (jsonify({'date_obj':date_obj}), 200)
