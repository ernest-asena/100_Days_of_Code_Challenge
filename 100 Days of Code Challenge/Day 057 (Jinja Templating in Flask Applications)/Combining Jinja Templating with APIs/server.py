from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)




@app.route('/')
def home():
    """Render website's home page."""
    year = datetime.datetime.now().year
    random_number = random.randint(99, 299)
    return render_template('index.html', num=random_number, cur_year=year)


@app.route('/guess/<name>')
def guess(name):
    """guess page"""
    gender_api = F'https://api.genderize.io?name={name}'
    age_url = F'https://api.agify.io?name={name}'
    age = requests.get(age_url).json()['age']
    gender = requests.get(gender_api).json()['gender']
    return render_template('guess.html', name=name, age=age, gender=gender)


app.run(debug=True, host='0.0.0.0', port=5002)
