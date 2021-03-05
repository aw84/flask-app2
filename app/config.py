class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/flaskapp2'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'


class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'test'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/flaskapp2_testing'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'


def get_config_by_name(name):
    if name.upper() == 'DEV':
        return DevelopmentConfig()
    elif name.upper() == 'TEST':
        return TestingConfig()
    else:
        raise Exception('Unable to find config name `{}\''.format(name))
