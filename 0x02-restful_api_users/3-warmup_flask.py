#!/usr/bin/python3
"""
3-warmup_flask: starts a Flask app
"""
from flask import (Flask, jsonify)
from os import getenv

app = Flask(__name__)
host = getenv('HBNB_API_HOST')
port = getenv('HBNB_API_PORT')
app.url_map.strict_slashes = False


@app.route('/hbtn/', strict_slashes=False)
def get_json():
    """ Returns jsonified response when route is called """
    dictionary = {
        "C": "is fun",
        "Python": "is cool",
        "Sysadmin": "is hiring"
    }
    return jsonify(dictionary)

if __name__ == "__main__":
    app.run(host=host, port=port)
