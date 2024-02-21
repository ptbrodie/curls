import peewee

from src.data.models.base import BaseModel
from src.data.models.api import API
from src.data.models.curl import Curl


class APICurlJoin(BaseModel):
    api = peewee.ForeignKeyField(API, on_delete='CASCADE')
    curl = peewee.ForeignKeyField(Curl, on_delete='CASCADE')

    class Meta:
        indexes = (
            (('api_id', 'curl_id'), True),
        )