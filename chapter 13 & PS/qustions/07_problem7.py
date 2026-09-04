'''
explore the flask module and create a web server using flask and pyhton 
'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()
