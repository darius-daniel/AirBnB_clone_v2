#!/usr/bin/python3
""" Starts a Flask Web Application """
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception=None):
    """ Removes the current SQLAlchemy Session """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def show_states(id=None):
    """ Render an HTML template """
    states = storage.all(State)

    states = storage.all(State)

    if not id:
        dict_to_html = {value.id: value.name for value in states.values()}
        return render_template(
            '7-states_list.html',
            Table="States",
            items=dict_to_html)

    st = "State.{}".format(id)
    if st in states:
        return render_template(
            '9-states.html',
            Table="State: {}".format(states[st].name),
            items=states[st])

    return render_template('9-states.html', items=None)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
