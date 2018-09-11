#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify
from models import db_session
from models.user import User


@app_views.route('/status')
def get_status():
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def get_stats():
    query = db_session.query(User)
    user_count = len([elem for elem in query])
    return jsonify({"users": user_count})
