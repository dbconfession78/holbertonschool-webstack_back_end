#!/usr/bin/python3
"""
app: api app file
"""
from flask import Flask, make_response, jsonify
from api.v1.views import app_views
from os import getenv
# from flask import jsonify
# from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
# CORS(app, resources={r"/*": {"origins": "0.0.0.0"}}) # <--


# @app.errorhandler(400)
# def page_not_found(e):
#     """ Returns a json object with a 400 response message  """
#     description = e.description
#     message = {'error': description}
#     return make_response(jsonify(message), 400)


# @app.errorhandler(404)
# def page_not_found(e):
#     """ Returns a json object with a 404 response message """
#     description = e.description
#     message = {'error': description}
#     return make_response(jsonify(message), 404)

# @app.teardown_appcontext
# def close_db(error):
#     """ Closes the databse at the end of the request """
#     db_session.remove()


if __name__ == "__main__":
    _host = getenv('HBNB_API_HOST', '0.0.0.0')
    _port = int(getenv('HBNB_API_PORT', 5050))
    app.run(host=_host, port=_port)
