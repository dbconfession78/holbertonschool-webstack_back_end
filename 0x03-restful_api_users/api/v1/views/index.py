#!/usr/bin/python3
"""
Module: index - contains the status and stats route for api
"""
from api.v1.views import app_views
from flask import jsonify, abort
from models import db_session
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """ Returns a json object with a status ok message  """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """ Returns a json object with a count of each object type  """
    retval = {}
    users = db_session.query(User)
    return jsonify({"users": len([x for x in users])})

@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized():
    """ aborts with a 401, 'unauthorized' """
    abort(401)

@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden():
    """ aborts with a 403, 'forbidden' """
    abort(403)
