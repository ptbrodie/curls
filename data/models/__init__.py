from data import DB
from data.models.api import API
from data.models.curl import Curl
from data.models.joins import APICurlJoin
from data.queries import api as aq


def init():
    DB.create_tables([API, Curl, APICurlJoin])
    try:
        API.get(name='default')
    except Exception as e:
        aq.new_api('default')
        aq.set_current('default')
