from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    """Home page with login form"""
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    """Receive data from the form and display it on the page."""
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {name}, Password: {password}</h1>"


app.run(debug=True, host='0.0.0.0')