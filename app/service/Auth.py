from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)


def sanitaze_user_input(data):
    # TODO: encoding, sanitaze, escape,...
    return data


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    user_name = sanitaze_user_input(data['user'])
    user_pass = sanitaze_user_input(data['pass'])
    
    

    return jsonify({
        'user': user_name,
        'pass': user_pass
    }), 200
