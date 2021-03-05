from app.celery import make_celery
from flask import current_app
from app.model.User import User


celery = make_celery(current_app)


@celery.task(bind=True)
def add(self, a, b):
    u = User.query.first()
    import sys
    print("---------------- {}".format(self.request.id))
    print("**************** {}".format(u.username if u is not None else 'X'))
    return a + b
