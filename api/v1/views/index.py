#!/usr/bin/python3
"""
This module contains endpoint(route) status
"""

from api.v1.views import app_views
from flask import jsonify

from models import storage

@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})

@app.route('/api/v1/stats', methods=['GET'])
def get_stats():
    data = {"amenities": 'Amenity',
            "cities": 'City',
            "places": 'Place',
            "reviews": 'Review',
            "states": 'State',
            "users": 'User'}

    for i in data.keys():
        data[i] = storage.count(data.get(i))
    return jsonify(data)
