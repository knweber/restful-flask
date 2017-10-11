## A RESTful Python web service built with Flask
Built for Pinterest's technical challenge

### Features:
  - Greetings
  - Mathematical operations
  - Current date
  
### Installation instructions
  1. Clone repo down to local computer: ```$ git clone https://github.com/knweber/restful-flask.git```
  2. Navigate into repo: ```$ cd restful-flask```
  3. Install dependencies: ```$ pip install -r requirements.txt```
  3. Run program: ```$ python main.py```
  4. Program runs on port 5000. To make a request, use one of the following url queries:
      - Greeting: ```localhost:5000/hello?firstname={first name}&lastname={last name}&gender={m/f}```
      - Operation: ```localhost:5000/compute?num1={num1}&num2={num2}&operator={add/subtract/multiply/divide}```
      - Get current date: ```localhost:5000/date```
  5. To run via the command line, use curl: ```$ curl -X GET http://localhost:5000/{your_query_here}```
  6. Run tests: ```$ python tests.py```

### Notes

I elected not to create ApiResponses/Computations/Greetings/Dates/etc. classes to store the functions in main.py, as I thought it was unnecessary given the size of my project. I wanted to keep my code as clear and concise as possible, and I figured that adding classes might lean toward over-engineering. If the instructions required functionality for POST/PUT/PATCH/DELETE requests, or if there were several more features included, I would definitely implement Resource classes.

### Original instructions

Build a simple REST-based web server in Scala or Python that supports the following features:
  - Respond to requests of the form ```/hello?firstname={first name}&lastname={last name}&gender={m/f}``` and respond with “Hello Mr {First Name} {Last Name}” or “Hello Ms {First Name} {Last Name}” depending on the gender
    - Example: the request ```/hello?firstname=tien&lastname=nguyen&gender=m``` returns “Hello Mr Tien Nguyen”
  - Respond to requests of the form ```/compute?num1={num1}&num2={num2}&operator={add/subtract/multiply/divide}``` and respond with the result
    - Example: the request ```/compute?num1=5&num2=3&operator=subtract``` returns “2” (5-3=2)
  - Respond to requests of the form ``/date`` with the current date in the form “yyyy-mm-dd”
    - Example: ``/date`` returns “2017-09-20”
