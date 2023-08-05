#!/usr/bin/python3
""" Starts a Flash Web Application """
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template, url_for
from models import storage
import uuid

"""flask setup"""
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


"""begin flask page rendering"""
@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/1-hbnb')
def hbnb_filters(the_id=None):
    """
    Custom template with states,amenities, and places with embedded cache_id
    """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    cache_id = (str(uuid.uuid4()))
    return render_template('100-hbnb.html',
                           states=states,
                           amens=amens,
                           places=places,
                           cache_id=cache_id)


if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)
