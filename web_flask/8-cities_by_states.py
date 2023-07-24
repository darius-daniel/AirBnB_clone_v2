#!/usr/bin/python3
"""
Starts a Flask application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception=None):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def ordered_cities_by_states():
    """ Displays an HTML Page """
    states = storage.all(State)
    return render_template(
        '8-cities_by_states.html', cls='States', states=states
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
