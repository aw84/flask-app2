from flask import Flask
from flask_migrate import Migrate

from app.config import get_config_by_name
from app.model.Model import *

migrate = Migrate()


def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(get_config_by_name(config_name))

    from app.model import db
    db.init_app(app)

    migrate.init_app(app, db)

    from app.service.Auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
