#!/usr/bin/python3
""" A script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception=None):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """ Display a HTML page """
    all_states = storage.all(State)
    states_dict = {value.id: value.name for value in all_states.values()}
    return render_template(
        '7-states_list.html', table='States', states=states_dict
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
