from functools import wraps
from sqlalchemy.orm import Session

from .model import get_engine


def session(func):
    @wraps(func)
    def open(self, *args, **kwargs):
        with Session(autoflush=True, bind=get_engine()) as db:
            return func(self, db, *args, **kwargs)

    return open