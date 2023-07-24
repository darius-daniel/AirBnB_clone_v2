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

    if not id:
        states_dict = {value.id: value.name for value in states.values()}
        return render_template(
            '7-states_list.html', table="States", states=states_dict
        )
    else:
        obj = f"State.{id}"
        if obj in states:
            return render_template(
                '9-states.html',
                table="State: {}".format(states[obj].name),
                states=states[obj]
            )

    return render_template('9-states.html', states=None)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
