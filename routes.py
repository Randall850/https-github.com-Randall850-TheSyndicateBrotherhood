from flask import Blueprint, jsonify

api_routes = Blueprint('api_routes', __name__)

@api_routes.route("/status", methods=["GET"])
def status():
    return jsonify({"message": "Syndicate AI is live."})