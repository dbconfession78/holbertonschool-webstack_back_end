#!/usr/bin/python3
from flask import (Flask, jsonify)
from os import getenv

app = Flask(__name__)
host = getenv('HBNB_API_HOST')
port = getenv('HBNB_API_PORT')
app.url_map.strict_slashes = False


@app.route('/hbtn')
def get_json():
    dictionary = {
        "C": "is_fun",
        "Python": "is cool",
        "Sysadmin": "is hiring"
    }
    return jsonify(dictionary)

if __name__ == "__main__":
    app.run(host=host, port=port)
