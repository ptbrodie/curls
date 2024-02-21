import peewee

from src.data.models.base import BaseModel


class Curl(BaseModel):
    timestamp = peewee.DateTimeField(constraints=[peewee.SQL('DEFAULT CURRENT_TIMESTAMP')])
    name = peewee.TextField(default=None, null=True)
    description = peewee.TextField(default=None, null=True)
    command = peewee.TextField()