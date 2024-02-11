import peewee

from src.data.models.base import BaseModel
from src.data.models.api import API
from src.data.models.curl import Curl


class APICurlJoin(BaseModel):
    api = peewee.ForeignKeyField(API)
    curl = peewee.ForeignKeyField(Curl)