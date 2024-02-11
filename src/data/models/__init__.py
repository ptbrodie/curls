from src.data import DB
from src.data.models.api import API
from src.data.models.curl import Curl
from src.data.models.joins import APICurlJoin
from src.data.queries import api as aq


def init():
    DB.create_tables([API, Curl, APICurlJoin])
    try:
        API.get(name='default')
    except Exception as e:
        aq.new_api('default')
        aq.set_current('default')
