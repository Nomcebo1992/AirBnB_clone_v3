#!/usr/bin/python3
"""
This module contains endpoint(route) status
"""
<<<<<<< HEAD
from models import storage
from flask import Flask
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """
    Returns a JSON status
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def count():
    """
    Retrieves the number of each objects by type
    """
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
=======

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
>>>>>>> e5925473bf644a0afe2f23df8524c204e9ef2598
