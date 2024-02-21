from datetime import datetime
import re
from uuid import uuid4

from src.data.models.api import API
from src.data.models.curl import Curl
from src.data.models.joins import APICurlJoin
from src.data.queries import curl as cq


def get_by_name(name):
    try:
        return API.get(name=name)
    except:
        return None


def get_by_id(id):
    try:
        return API.get(id=id)
    except:
        return None


def delete(id):
    return API.delete().where(API.id==id).execute()


def list_apis():
    q = API.select().order_by(API.date_created)
    return [a for a in q]
    

def validate_name(name):
    return not re.match(r'.*\s.*', name)

def new_api(name, current=False):
    if not validate_name(name):
        raise Exception('Name invalid: spaces not allowed')
    api = get_by_name(name)
    if api:
        return None
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
    qs = [cq.get_by_id, cq.get_by_name]
    for q in qs:
        curl = q(curl_id)
        if curl:
            APICurlJoin.create(id=id, api=api, curl=curl)
            return True
    return False


def remove_from_api(api, curl_id):
    qs = [cq.get_by_id, cq.get_by_name]
    for q in qs:
        curl = q(curl_id)
        if curl:
            q = APICurlJoin.delete().where(APICurlJoin.api_id==api.id, APICurlJoin.curl_id==curl.id)
            q.execute()
            return True
    return False


def to_json(api):
    curls = get_curls(api)
    result = {
        "id": api.id,
        "name": api.name,
        "date_created": api.date_created.isoformat(),
        "curls": [cq.to_json(c) for c in curls]
    }
    return result


def delete_all():
    return API.delete().execute()