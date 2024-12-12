from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# instantiate application

#python decorator
#In this case, @app.route is a Python decorator. Decorators take functions and returns another function, usually extending the input function with additional 
#("decorated") functionality. @app.route is a decorator that takes an input function index() as the callback that gets invoked when a request to route / comes in from a client
@app.route('/')

app = Flask(__name__)
# index is the standard name for route handlers that listens for 
# connection to the route and figures out what to do next
def index():
    # return a string
    return 'Hello World!'

#always include this at the bottom of your code
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
