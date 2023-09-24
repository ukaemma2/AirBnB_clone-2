#!/usr/bin/python3
"""Starts Flask web apllication."""
from flask import Flask
app = Flask(__name__)
'''Define the route for the root URL '/'
'''

@app.route('/', strict_slashes=False)


def hello_HBNB():
    '''Display 'Hello HBNB! '''
    return "Hello HBNB!"


if __name__ == "__main__":
    '''Start the Flash development server
    Listen on all available network interfaces (0.0.0.0) and port 5000
    '''
    app.run(host='0.0.0.0')
