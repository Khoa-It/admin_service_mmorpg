from flask import Blueprint, jsonify

admin_routes = Blueprint('admin', __name__)

@admin_routes.route("/hello", methods=["GET"])
def hello():
    return jsonify({
        'message' : 'hello this is admin service',
        'data' : None,
    })

