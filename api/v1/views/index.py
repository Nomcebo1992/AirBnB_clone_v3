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
    counts = storage.count()
    return jsonify(counts)
