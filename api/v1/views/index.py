#!/usr/bin/python3
"""
This module contains endpoint(route) status
"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def get_status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})
