from datetime import datetime
import peewee

from src.data.models.base import BaseModel


class API(BaseModel):
    name = peewee.CharField(unique=True)
    date_created = peewee.DateTimeField(constraints=[peewee.SQL('DEFAULT CURRENT_TIMESTAMP')])
    date_current = peewee.DateTimeField(default=datetime(1900, 1, 1))