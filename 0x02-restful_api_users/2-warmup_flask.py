#!/usr/bin/python3
"""
2-warmup_flask: start's a Flask application
"""
from flask import Flask

app = Flask(__name__)
host = '0.0.0.0'
port = 5000
app.url_map.strict_slashes = False


@app.route('/')
def get_hbs_string():
    """ Returns 'Holberton School' when the route is called """
    return "Holberton School"


@app.route('/c')
def get_c_string():
    """ Return's 'C is fun!' when the route is called """
    return "C is fun!"


if __name__ == "__main__":
    app.run(host=host, port=port)
