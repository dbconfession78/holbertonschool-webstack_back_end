#!/usr/bin/python3
"""
app: api app file
"""
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from flask import Flask, make_response, jsonify, request, abort
from api.v1.views import app_views
from models import db_session
from os import getenv


app = Flask(__name__)
auth = BasicAuth() if getenv('HBNB_YELP_AUTH') == 'basic_auth' else Auth()
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    """ Closes the databse at the end of the request """
    db_session.remove()


@app.errorhandler(403)
def unauthorized(e):
    """ Returns a json object sith a 401 rsponse message """
    return make_response(jsonify({'error': 'Forbidden'}), 403)


@app.errorhandler(401)
def unauthorized(e):
    """ Returns a json object sith a 401 rsponse message """
    return make_response(jsonify({'error': 'Unauthorized'}), 401)


@app.errorhandler(404)
def page_not_found(e):
    """ Returns a json object with a 404 response message """
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def page_not_found(e):
    """ Returns a json object with a 400 response message  """
    description = e.description
    message = {'error': description}
    return make_response(jsonify(message), 400)


@app.before_request
def before_request():
    """ Handles authorization before request"""
    excluded_paths = ['/api/v1/status/',
                      '/api/v1/unauthorized/',
                      '/api/v1/forbidden/',
                      '/api/v1/users_delete/']

    if not auth.require_auth(request.path, excluded_paths):
        return

    if not auth.authorization_header(request):
        abort(401)
    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    _host = getenv('HBNB_API_HOST', '0.0.0.0')
    _port = int(getenv('HBNB_API_PORT', 5050))
    app.run(host=_host, port=_port)
