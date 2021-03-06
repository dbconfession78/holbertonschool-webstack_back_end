#!/usr/bin/python3
"""
1-warmup_flask: start's a Flask app
"""
from flask import Flask

app = Flask(__name__)
host = "0.0.0.0"
port = 5000


@app.route('/c')
def get_c_string():
    """ Return's 'C is fun!' when the route is called' """
    app.url_map.strict_slashes = False
    return "C is fun!"


if __name__ == "__main__":
    app.run(host=host, port=port)
