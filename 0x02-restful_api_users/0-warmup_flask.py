#!/usr/bin/python3
"""
0-warmup_flask: starts an app
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def fetch():
    """ Returns 'Holberton School' when the '/' route is called """
    app.url_map.strict_slashes = False
    return "Holberton School"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
