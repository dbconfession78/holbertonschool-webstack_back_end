from api.v1.views import app_views
from models import db_session
from models.user import User
from flask import (jsonify, abort)


@app_views.route('/users')
def get_users():
    """ Gets list of  all user dictionaries  """
    user_dict = get_all_users()
    user_dicts = []
    for value in user_dict.values():
        user_dicts.append(value.to_dict())
    return jsonify(user_dicts)


@app_views.route('/users/<user_id>')
def get_user(user_id):
    """ Gets dictionary representation of single user """
    user_dict = get_all_users()
    user = user_dict.get(user_id)
    if user:
        return jsonify(user.to_dict())
    abort(404, 'Not found')


def get_all_users():
    """ returns a k/v dict of users refernced by user id """
    users_dict = {}
    user_objects = db_session.query(User)
    for user_object in user_objects:
        users_dict[user_object.id] = user_object
    return users_dict
