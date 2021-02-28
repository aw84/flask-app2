class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/flaskapp2'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/flaskapp2_testing'


def get_config_by_name(name):
    if name.upper() == 'DEV':
        return DevelopmentConfig()
    elif name.upper() == 'TEST':
        return TestingConfig()
    else:
        raise Exception('Unable to find config name `{}\''.format(name))
