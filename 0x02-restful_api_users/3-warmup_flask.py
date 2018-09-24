#!/usr/bin/python3
"""
3-warmup_flask: starts a Flask app
"""
from flask import (Flask, jsonify)
from os import getenv

app = Flask(__name__)


@app.route('/hbtn', strict_slashes=False)
def get_json():
    """ Returns jsonified response when route is called """
    app.url_map.strict_slashes = False
    dictionary = {
        "C": "is fun",
        "Python": "is cool",
        "Sysadmin": "is hiring"
    }
    return jsonify(dictionary)

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = int(getenv('HBNB_API_PORT'))
    app.run(host=host, port=port)
