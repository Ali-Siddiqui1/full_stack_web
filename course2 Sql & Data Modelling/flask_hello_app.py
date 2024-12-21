from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# instantiate application

#Flask is a class allows us to create an application
# __name_ that gets named after the name of file which app.py 
app = Flask(__name__)

# setup a route to listen to our homepage
@app.route('/')
# index is the standard name for route handlers that listens for 
# connection to the route and figures out what to do next
def index():
    # return a string
    return 'Hello World!'

#always include this at the bottom of your code
if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5001)
