#!/usr/bin/python3
from api.v1.views import app_views
from flask import (jsonify, abort, request)
from models.user import User
from models import db_session
from datetime import datetime


@app_views.route('/users', strict_slashes=False)
def get_users():
    """ Gets list of  all user dictionaries  """
    user_dicts = []
    all_users = get_users_dictionary()
    for value in all_users.values():
        user_dicts.append(value.to_dict())
    return jsonify(user_dicts)


# @app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
# def update(user_id):
#     all_users = get_users_dictionary()
#     if user_id not in all_users:
#         abort(404, 'Not found')

#     request_body = request.get_json()
#     if not request_body:
#         return jsonify({"error": "Wrong format"})

#     user_obj = all_users.get(user_id)
#     for k, v in request_body.items():
#         if k in ('first_name', 'last_name'):
#             user_obj.__setattr__(k, request_body.get(k))
#     user_obj.updated_at = datetime.utcnow()

#     db_session.add(user_obj)
#     db_session.commit()
#     del user_obj.__dict__['_password']
#     return jsonify(user_obj.to_json()), 200


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


# @app_views.route('/users/',
#                  methods=['POST'],
#                  strict_slashes=False)
# def post():
#     if request.method == 'POST':
#         req_json = request.get_json()

#         if not req_json:
#             abort(400, 'Wrong format')

#         email = req_json.get("email")
#         password = req_json.get("password")

#         if not email:
#             abort(400, 'email missing')
#         if not password:
#             abort(400, 'password missing')

#         new_obj = User(**req_json)
#         db_session.add(new_obj)
#         db_session.commit()
#         del new_obj.__dict__['_password']
#         return jsonify(new_obj.to_json()), 201


def get_users_dictionary():
    """ returns a k/v dict of users refernced by user id """
    users_dict = {}
    user_objects = all()

    for user_object in user_objects.values():
        users_dict[user_object.id] = user_object

    return users_dict


def all():
    """ Returns a dictionary of all users """
    obj_dict = {}
    a_query = db_session.query(User)
    for obj in a_query:
        obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
        obj_dict[obj_ref] = obj
    return obj_dict
