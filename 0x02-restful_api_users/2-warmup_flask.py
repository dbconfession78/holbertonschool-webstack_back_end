#!/usr/bin/python3
"""
2-warmup_flask: start's a Flask application
"""
from flask import Flask
from os import getenv

app = Flask(__name__)


@app.route('/')
def get_hbs_string():
    """ Returns 'Holberton School' when the route is called """
    app.url_map.strict_slashes = False
    return "Holberton School"


@app.route('/c', strict_slashes=False)
def get_c_string():
    """ Return's 'C is fun!' when the route is called """
    app.url_map.strict_slashes = False
    return "C is fun!"


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = int(getenv('HBNB_API_PORT'))
    app.run(host=host, port=port)
