#!/usr/bin/python3
from api.v1.views import app_views
from os import getenv
from flask import (Flask, jsonify)


app = Flask(__name__)
host = getenv('HBNB_API_HOST')
port = getenv('HBNB_API_PORT')
app.register_blueprint(app_views)


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "not found"})


if __name__ == "__main__":
    app.run(host=host, port=port)
