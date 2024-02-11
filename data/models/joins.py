import peewee

from data.models.base import BaseModel
from data.models.api import API
from data.models.curl import Curl


class APICurlJoin(BaseModel):
    api = peewee.ForeignKeyField(API)
    curl = peewee.ForeignKeyField(Curl)