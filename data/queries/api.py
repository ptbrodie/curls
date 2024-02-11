from datetime import datetime
from uuid import uuid4

from data.models.api import API
from data.models.curl import Curl
from data.models.joins import APICurlJoin


def get_by_name(name):
    return API.get(name=name)


def list_apis():
    q = API.select().order_by(API.date_created)
    return [a for a in q]
    

def new_api(name, current=False):
    id = str(uuid4()).replace('-', '')
    date_current = datetime.now() if current else datetime(1970, 1, 1)
    api = API.create(id=id, name=name, date_current=date_current)
    return api


def get_current():
    return [a for a in API.select().order_by(-API.date_current)][0]


def set_current(name):
    try:
        api = API.get(name=name)
        api.date_current = datetime.now()
        api.save()
        return True
    except Exception as e:
        return False
    

def get_curls(api):
    q = (Curl
         .select()
         .join(APICurlJoin)
         .join(API)
         .where(API.name == api.name))
    return [c for c in q]


def add_to_api(api, curl_id):
    id = str(uuid4()).replace('-', '')
    curl = Curl.get_by_id(curl_id)
    APICurlJoin.create(id=id, api=api, curl=curl)
    return True


def delete_from_api(api, curl_id):
    curl = Curl.get_by_id(curl_id)
    q = APICurlJoin.delete().where(APICurlJoin.api_id==api.id, APICurlJoin.curl_id==curl.id)
    q.execute()
