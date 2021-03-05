from app.celery import tasks
from flask import Blueprint, jsonify, request
from flask_restplus import Namespace, Resource, fields
from app.model import db
from app.model.User import User


ns = Namespace('User', description='User description')

login_model = ns.model('UserCreateModel', {
    'user': fields.String(required=True, description='name'),
    'email': fields.String(required=True, description='email'),
})


def sanitaze_user_input(data):
    # TODO: encoding, sanitaze, escape,...
    return data


@ns.route('/')
class Create(Resource):
    @ns.expect(login_model)
    def post(self,):
        data = request.get_json()

        user_name = sanitaze_user_input(data['user'])
        user_email = sanitaze_user_input(data['email'])
        try:
            u1 = User(username=user_name, email=user_email)

            db.session.add(u1)
            db.session.commit()
        except:
            db.session.rollback()

        u = User.query.filter(User.username == user_name).first()

        return {
            'user': u.username,
            'email': u.email
        }, 200


@ns.route('/<user>')
@ns.doc(params={'user': 'username'})
class ShowUser(Resource):
    def get(self, user):
        u = User.query.filter(User.username == user).first()
        return u.username if u is not None else 'X', 200
