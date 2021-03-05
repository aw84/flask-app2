from flask import Blueprint, request, jsonify
from app.celery import tasks


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


@auth_bp.route('/async', methods=['GET'])
def async_add():
    r = tasks.add.apply_async(args=(1,2), queue='flaskapp2')
    import sys
    print(r.task_id, flush=True, file=sys.stderr)
    return 'OK', 200
