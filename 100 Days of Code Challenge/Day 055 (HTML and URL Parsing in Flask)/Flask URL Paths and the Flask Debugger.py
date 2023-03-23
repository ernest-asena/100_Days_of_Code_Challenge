from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """This is the home page"""
    return "Hello World."


@app.route('/bye')
def bye():
    """This is the goodbye page"""
    return "It is sad to see you leave. Hopefully we will reconnect soon."


@app.route('/username/<name>/<number>')
def greet(name, number):
    return F"Hello there {name}!\nYou are {number} years old"


# Creating variable paths and converting the path to a specified data type
@app.route('/leaders/<leader>/<int:number>')
def greet_leader(leader, number):
    return F"Greetings Leader. You are {number} today!"


app.run(debug=True)
