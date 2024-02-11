import peewee

from src.data.models.base import BaseModel


class Curl(BaseModel):
    timestamp = peewee.DateTimeField(constraints=[peewee.SQL('DEFAULT CURRENT_TIMESTAMP')])
    command = peewee.TextField()