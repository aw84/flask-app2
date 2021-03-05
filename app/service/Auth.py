from app.celery import tasks
from flask import Blueprint, jsonify, request
from flask_restplus import Namespace, Resource, fields

auth_ns = Namespace('auth', description='Authorization description')

login_model = auth_ns.model('LoginModel', {
    'id': fields.String(required=True, description='The cat identifier'),
    'pass': fields.String(required=True, description='The cat name'),
})


def sanitaze_user_input(data):
    # TODO: encoding, sanitaze, escape,...
    return data


@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(login_model)
    def post(self,):
        data = request.get_json()

        user_id = sanitaze_user_input(data['id'])
        user_pass = sanitaze_user_input(data['pass'])

        return {
            'user': user_id,
            'pass': user_pass
        }, 200


@auth_ns.route('/async', methods=['GET'])
class AsyncAdd(Resource):
    def get(self,):
        r = tasks.add.apply_async(args=(1, 2), queue='flaskapp2')
        import sys
        print(r.task_id, flush=True, file=sys.stderr)
        return 'OK', 200
