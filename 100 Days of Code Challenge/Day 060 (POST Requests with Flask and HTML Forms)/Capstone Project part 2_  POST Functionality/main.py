from flask import Flask, render_template, request
import smtplib
import requests
import config

posts = requests.get("https://api.npoint.io/2c5f2999ffe9dbddf8b7").json()
OWN_EMAIL = config.my_email
OWN_PASSWORD = config.password
app = Flask(__name__)

@app.route('/')
def get_all_posts():
    """Create home page with all blog posts"""
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    """Shows post with the corresponding id, like /post/1, /post/2, etc."""
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    """About page"""
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Contact page with a contact form"""
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    """Send email to my email address"""
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


app.run(debug=True, host='0.0.0.0')
