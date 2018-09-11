#!/usr/bin/python3
from api.v1.views import app_views
from os import getenv
from flask import (Flask, jsonify)
from models import db_session

app = Flask(__name__)
host = getenv('HBNB_API_HOST')
port = getenv('HBNB_API_PORT')
app.register_blueprint(app_views)


@app.errorhandler(404)
def page_not_found(e):
    """ Returns a json object indicating the page couldn't be found  """
    return jsonify({"error": "Not found"})

@app.teardown_appcontext
def close_db(error):
    """ Closes the databse at the end of the request """
    db_session.remove()

if __name__ == "__main__":
    app.run(host=host, port=port)
