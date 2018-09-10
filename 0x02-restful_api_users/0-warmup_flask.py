#!/usr/bin/python3
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False
host = '0.0.0.0'
port = 5000


@app.route('/')
def fetch():
    return "Holberton School"

if __name__ == "__main__":
    app.run(host=host, port=port)
