#!/usr/bin/python3
""" Starts  a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask, request

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_HBNB():
    """Display 'HBNB'"""
    return "HBNB"


'''Define route for "/c/<text>"'''
@app.route("/c/<text>", strict_slashes=False)
def c_with_text(text):
    """Define "C" followed by by the value of <texyt>.
    Replace underscores with spaces in the text variable
    """
    formatted_text = text.replace("_", " ")
    return "C {}".format(formatted_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
