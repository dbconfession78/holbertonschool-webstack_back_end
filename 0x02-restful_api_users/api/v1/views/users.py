#!/usr/bin/python3
"""
module: User api
"""
from api.v1.views import app_views
from flask import (jsonify, abort, request)
from models.user import User
from models import db_session
from datetime import datetime


@app_views.route('/users/', methods=['GET'], strict_slashes=False)
def get_users():
    """ Returns all users in JSON format  """
    users = []
    for user in all().values():
        del user._password
        users.append(user.to_json())
    return jsonify(users)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update(user_id):
    """ Updates a user record """
    if user_id is None:
        abort(404)

    all_obj = all()
    _id = "User.{}".format(user_id)
    user = all_obj.get(_id)
    if user is None:
        abort(404)

    try:
        request_body = request.get_json()
    except:
        request_body = None

    if request_body is None:
        return jsonify({"error": "Wrong format"})

    for item in ("id", "created_at", "updated_at", "email"):
        request_body.pop(item, None)
    for k, v in request_body.items():
        setattr(user, k, v)
    db_session.add(user)
    db_session.commit()
    if '_password' in user.__dict__:
        del user.__dict__['_password']
    return jsonify(user.to_json()), 200

    # request_body = request.get_json()
    # if not request_body:
    #     return jsonify({"error": "Wrong format"})

    # user_obj = all_obj.get("User.{}".format(user_id))
    # for k, v in request_body.items():
    #     if k in ('first_name', 'last_name'):
    #         user_obj.__setattr__(k, request_body.get(k))
    # user_obj.updated_at = datetime.utcnow()

    # db_session.add(user_obj)
    # db_session.commit()
    # del user_obj.__dict__['_password']
    # return jsonify(user_obj.to_json()), 200


@app_views.route('/users/<user_id>',
                 methods=['GET'],
                 strict_slashes=False)
def get_single_user(user_id):
    """ Returns a user object in JSON format """
    try:
        all_obj = all()
        _id = "User.{}".format(user_id)
        user = all_obj.get(_id)

        del user._password
        return jsonify(user.to_json())
    except:
        abort(404)


@app_views.route('/users/delete_all',
                 methods=['GET'],
                 strict_slashes=False)
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


@app_views.route('/users/<user_id>',
                 methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """ Deletes a single user record """
    try:
        all_obj = all()
        _id = "User.{}".format(user_id)
        user = all_obj.get(_id)

        db_session.delete(user)
        db_session.commit()
        return jsonify({}), 200
    except:
        abort(404)


# @app_views.route('/users/<user_id>',
#                  methods=['GET', 'DELETE'], strict_slashes=False)
# def get_user(user_id):
#     """ Gets dictionary representation of single user """
#     all_users = get_users_dictionary()
#     user_obj = all_users.get(user_id)

#     if not user_obj:
#         abort(404, 'Not found')

#     if request.method == 'GET':
#         return jsonify(user_obj.to_dict())

#     if request.method == 'DELETE':
#         db_session.delete(user_obj)
#         db_session.commit()
#         return jsonify({}), 200


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


# def get_users_dictionary():
#     """ returns a k/v dict of users refernced by user id """
#     users_dict = {}
#     user_objects = all()

#     for user_object in user_objects.values():
#         users_dict[user_object.id] = user_object

#     return users_dict


def all():
    """ Returns a dictionary of all users """
    obj_dict = {}
    a_query = db_session.query(User)
    for obj in a_query:
        obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
        obj_dict[obj_ref] = obj
    return obj_dict
