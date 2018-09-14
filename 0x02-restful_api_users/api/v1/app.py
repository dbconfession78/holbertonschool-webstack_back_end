#!/usr/bin/python3
from api.v1.views import app_views
from flask import (Flask, jsonify, make_response)
from models import db_session
from os import getenv


app = Flask(__name__)
app.url_map.strict_slashes = False
host = getenv('HBNB_API_HOST')
port = getenv('HBNB_API_PORT')
app.register_blueprint(app_views)


@app.errorhandler(400)
def page_not_found(e):
    """ Returns a json object with a 400 response message  """
    description = e.description
    message = {'error': description}
    return make_response(jsonify(message), 400)


@app.errorhandler(404)
def page_not_found(e):
    """ Returns a json object with a 404 response message """
    description = e.description
    message = {'error': description}
    return make_response(jsonify(message), 404)


@app.teardown_appcontext
def close_db(error):
    """ Closes the databse at the end of the request """
    db_session.remove()


if __name__ == "__main__":
    app.run(host=host, port=port)
