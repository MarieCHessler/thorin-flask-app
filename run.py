"""
Import os
Import JSon
Import Flask class from Flask
"""
import os
import json
from flask import Flask, render_template  # Import Flask class

# Store an instance of the class in the variable app
# Set argument __name__, for Flask to know where to look
# for templates and static files
app = Flask(__name__)


@app.route("/")
def index():
    """
    Return index.html template
    Decorator that starts with @ wraps function
    """
    return render_template("index.html")  # Get info from template


@app.route("/about")
def about():
    """
    Return about.html template
    """
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    """
    Create path to get and return more info on each character
    """
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)
    # To test if clicking the name works:
    # return "<h1>" + member["name"] + "</h1>"


@app.route("/contact")
def contact():
    """
    Return contact.html template
    """
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    """
    Return contact.html template
    """
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":  # __main__ is the default module in Python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)  # Makes it much easier to debug during development.
# Change to False before submit!
