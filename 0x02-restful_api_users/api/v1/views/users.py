#!/usr/bin/python3
"""
module: User api
"""
from api.v1.views import app_views
from flask import (jsonify, abort, request)
from models.user import User
from models import db_session
from datetime import datetime


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():
    """ Returns all users in JSON format  """
    users = []
    for user in all().values():
        del user._password
        users.append(user.to_json())
    return jsonify(users)


@app_views.route('/users/<user_id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def modify_single_user(user_id):
    """ Modifies and/or returns a single user record in JSON format """
    if user_id is None:
        abort(404)
    _id = "User.{}".format(user_id)
    user_obj = all().get(_id)
    if request.method == 'GET':
        try:
            del user_obj._password
            return jsonify(user_obj.to_json())
        except:
            abort(404)

    if request.method == 'DELETE':
        try:
            db_session.delete(user_obj)
            db_session.commit()
            return jsonify({}), 200
        except:
            abort(404)

    if request.method == 'PUT':
        request_body = request.get_json()
        if request_body is None:
            return jsonify({"error": "Wrong format"})

        for item in ("id", "created_at", "updated_at", "email"):
            request_body.pop(item, None)
        for k, v in request_body.items():
            setattr(user_obj, k, v)
        db_session.add(user_obj)
        db_session.commit()
        if '_password' in user_obj.__dict__:
            del user_obj.__dict__['_password']
        return jsonify(user_obj.to_json()), 200

    return jsonify(user_obj.to_json()), 200


@app_views.route('/users/*', methods=['DELETE'], strict_slashes=False)
def delete_all_users():
    """ Deletes all user records """
    all_obj = all()
    try:
        for k, v in all_obj.items():
            user = all_obj.get(k)
            db_session.delete(user)
        db_session.commit()
    except:
        raise Exception("couldn't delete 1 or more user records, rolling back")
    return jsonify({}), 200


@app_views.route('/users',
                 methods=['POST'],
                 strict_slashes=False)
def post():
    """ Adds a user record """
    req_json = request.get_json()

    if not req_json:
        abort(400, 'Wrong format')

    email = req_json.get("email")
    password = req_json.get("password")

    if not email:
        abort(400, 'email missing')
    if not password:
        abort(400, 'password missing')

    new_obj = User(**req_json)
    db_session.add(new_obj)
    db_session.commit()
    del new_obj.__dict__['_password']
    if 'first_name' not in new_obj.__dict__:
        new_obj.__dict__['first_name'] = None
    if 'last_name' not in new_obj.__dict__:
        new_obj.__dict__['last_name'] = None

    return jsonify(new_obj.to_json()), 201


def all():
    """ Returns a dictionary of all users """
    obj_dict = {}
    a_query = db_session.query(User)
    for obj in a_query:
        obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
        obj_dict[obj_ref] = obj
    return obj_dict
