#!/usr/bin/python3
"""
Starts a Flask application
"""
from flask import Flask, render_template
from models import storage
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception=None):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    cities = storage.all(City)
    cities_dict = {city.id: city.name for city in cities.keys().sorted()}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
