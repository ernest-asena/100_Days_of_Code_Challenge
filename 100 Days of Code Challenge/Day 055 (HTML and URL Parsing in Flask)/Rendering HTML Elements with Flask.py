from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """This is the home page"""
    return '<h1>Hello World</h1><p>This is a simple paragraph to say that we are happy with Flask.<br> Laca is actually ' \
           'dancing just to prove it. Trust Laca!<p>' \
           '<img src="https://media.giphy.com/media/ORVArZlFq0DSyVJ6C8/giphy.gif">'


app.run(debug=True)
