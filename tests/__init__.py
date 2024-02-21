from src.data import models
from src.data.queries import curl as cq, api as aq

models.init()


def clean_setup(func):
    def decorator(*args, **kwargs):
        cq.delete_all()
        aq.delete_all()
        models.init()
        func(*args, **kwargs)
        cq.delete_all()
        aq.delete_all()
        models.init()
    return decorator