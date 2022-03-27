"""
Import os
Import Flask class from Flask
"""
import os
from flask import Flask, render_template  # Import Flask class

# Store an instance of the class in the variable app
# Set argument __name__, for Flask to know where to look
# for templates and static files
app = Flask(__name__)


@app.route("/")
def index():
    """
    Returns index.html template
    Decorator - starts with @, used to wrap function
    """
    return render_template("index.html")  # Get info from template


@app.route("/about")
def about():
    """
    Returns about.html template
    Decorator - starts with @, used to wrap function
    """
    return render_template("about.html", page_title="About")


@app.route("/contact")
def contact():
    """
    Returns contact.html template
    Decorator - starts with @, used to wrap function
    """
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    """
    Returns contact.html template
    Decorator - starts with @, used to wrap function
    """
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":  # __main__ is the default module in Python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)  # Makes it much easier to debug during development.
# Change to False before submit!
