## A RESTful web service built in Python that responds to three types of requests:
  - Greetings
  - Mathematical operations
  - Current date
  
## Installation instructions

## Notes

## Original instructions

Build a simple REST-based web server in Scala or Python that supports the following features:
  - Respond to requests of the form “/hello?firstname={first name}&lastname={last name}&gender={m/f}” and respond with “Hello Mr {First Name} {Last Name}” or “Hello Ms {First Name} {Last Name}” depending on the gender
    - Example: the request “/hello?firstname=tien&lastname=nguyen&gender=m” returns “Hello Mr Tien Nguyen”
  - Respond to requests of the form “/compute?num1={num1}&num2={num2}&operator={add/subtract/multiply/divide}” and respond with the result
    - Example: the request “/compute?num1=5&num2=3&operator=subtract” returns “2” (5-3=2)
  - Respond to requests of the form “/date” with the current date in the form “yyyy-mm-dd”
    - Example: “/date” returns “2017-09-20”
