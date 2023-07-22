#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask, abort


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Displays a message when the index page is requested
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays a message when the @hbnb page is requested
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays a message when the @c/text page is requested
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_text(text="is_cool"):
    """ Displays a message when the @python/(<text>) is requested
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<n>', strict_slashes=False)
def num_text(n):
    """ Displays a message when the @number page is requested
    """
    try:
        int(n)
    except Exception:
        abort(404)
    else:
        return "n is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
