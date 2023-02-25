from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/2c5f2999ffe9dbddf8b7").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    """Get all post objects"""
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    """Get all post objects"""
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    """about page"""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """contact page"""
    return render_template("contact.html")

app.run(debug=True, host='0.0.0.0')
