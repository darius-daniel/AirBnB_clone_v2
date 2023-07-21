#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask, render_template


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
        pass
    else:
        return "n is a number"


@app.route('/number_template/<n>', strict_slashes=False)
def num_temp_text(n):
    """
    Display a HTML page if @n is an integer
    """
    try:
        int(n)
    except Exception:
        pass
    else:
        return render_template('5-number.html', number=int(n))


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def odd_or_even(n):
    """ Display a HTML page only if @n is an integer
    """
    try:
        int(n)
    except Exception:
        pass
    else:
        n = int(n)
        string = 'odd'
        if n % 2 == 0:
            string = 'even'
        return render_template('6-number_odd_or_even.html', number=n, div_by_2=string)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
