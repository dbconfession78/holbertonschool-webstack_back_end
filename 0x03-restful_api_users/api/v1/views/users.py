#!/usr/bin/python3
"""
module: User api
"""
from api.v1.views import app_views
from flask import (jsonify, abort, request)
from models.user import User
from models import db_session


@app_views.route('/users/', methods=['GET'], strict_slashes=False)
def get_users():
    """ Returns all users in JSON format  """
    users = []
    for user in all().values():
        del user._password
        users.append(user.to_json())
    return jsonify(users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_single_user(user_id):
    """ Returns a user object in JSON format """
    try:
        all_obj = all()
        _id = "User.{}".format(user_id)
        user = all_obj.get(_id)

        del user._password
        return jsonify(user.to_json())
    except Exception:
        abort(404)


@app_views.route('/users_delete', methods=['DELETE'], strict_slashes=False)
def delete_all_users():
    """ Deletes all user records """
    try:
        users = all()
        for user in users.values():
            db_session.delete(user)
        db_session.commit()
        return jsonify({}), 200
    except Exception:
        abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """ Deletes a single user record """
    try:
        all_obj = all()
        _id = "User.{}".format(user_id)
        user = all_obj.get(_id)

        db_session.delete(user)
        db_session.commit()
        return jsonify({}), 200
    except Exception:
        abort(404)


@app_views.route('/users/', methods=['POST'], strict_slashes=False)
def post():
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
    if email_exists(email):
        abort(400, 'email already exists')

    db_session.add(new_obj)
    db_session.commit()
    del new_obj.__dict__['_password']
    if 'first_name' not in new_obj.__dict__:
        new_obj.__dict__['first_name'] = None
    if 'last_name' not in new_obj.__dict__:
        new_obj.__dict__['last_name'] = None

    return jsonify(new_obj.to_json()), 201


def email_exists(email):
    """  Returns True if the email exists in the database """
    q = db_session.query(User).filter(User.email == email)
    return q.count() != 0


def all():
    """ Returns a dictionary of all users """
    obj_dict = {}
    a_query = db_session.query(User)
    for obj in a_query:
        obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
        obj_dict[obj_ref] = obj
    return obj_dict
