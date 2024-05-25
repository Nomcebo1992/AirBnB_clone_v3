#!/usr/bin/python3
"""
This module contains endpoint(route) status
"""

from api.v1.views import app_views
from flask import jsonify

from models import storage

@app_views.route('/status', methods=['GET'])
def get_status():
    """
    Status Route
    return: Response with JSON
    """
    return jsonify({"status": "OK"})

@app.route('/stats', methods=['GET'])
def get_stats():
    """
    stats of all obj routes
    """
    data = {
            "amenities": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User"),
            }

    return jsonify(data)
