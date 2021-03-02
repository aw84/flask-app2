from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/', methods=['POST'])
def login():
    data = request.get_json()
    return jsonify(data), 200
