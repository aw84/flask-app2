from flask import Blueprint
from flask_restplus import Api

from .Auth import auth_ns
from .User import ns as user_ns


blueprint = Blueprint('api', __name__, url_prefix='/v1')

api = Api(blueprint,
          title='Test title',
          version='0.1',
          description='A test description'
          )

api.add_namespace(auth_ns)
api.add_namespace(user_ns)
