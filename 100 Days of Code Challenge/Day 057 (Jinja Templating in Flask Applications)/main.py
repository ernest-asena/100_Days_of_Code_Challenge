from flask import Flask, render_template
app = Flask(__name__)
import random
import datetime


@app.route('/')
def home():
    year = datetime.datetime.now().year
    random_number = random.randint(99,299)
    return render_template('index.html', num=random_number, cur_year=year)


app.run(debug=True)