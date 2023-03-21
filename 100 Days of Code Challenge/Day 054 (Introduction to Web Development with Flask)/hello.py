from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Return a string"""
    return "<p>Hello, World! I am Ernest Asena.</p>"


app.run()
