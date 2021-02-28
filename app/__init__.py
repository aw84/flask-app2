from flask import Flask

from app.config import get_config_by_name


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(get_config_by_name('DEV'))

    from app.model import db
    db.init_app(app)

    return app
