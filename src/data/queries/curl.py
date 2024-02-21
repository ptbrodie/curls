from uuid import uuid4 

from src.data.models.curl import Curl


def get_by_id(id):
    try:
        return Curl.get(id=id)
    except:
        return None


def get_by_name(name):
    try:
        return Curl.get(name=name)
    except:
        return None


def delete(id):
    return Curl.delete().where(Curl.id==id).execute()


def get_history():
    q = Curl.select().order_by(Curl.timestamp)
    return [c for c in q]


def save_history(cmd):
    id = str(uuid4()).replace('-', '')
    curl = Curl.create(id=id, command=cmd)
    curl.save()
    return curl


def new_curl(command, timestamp):
    id = str(uuid4()).replace('-', '')
    curl = Curl.create(id=id, command=command, timestamp=timestamp)
    curl.save()
    return curl


def delete_curl(id):
    curl = get_by_id(id)
    curl.delete_instance()
    return True


def add_metadata(id, name=None, description=None):
    curl = get_by_id(id)
    if not curl:
        return None
    if name:
        curl.name = name
    if description:
        curl.description = description
    curl.save()
    return curl


def to_json(curl):
    return {
        "id": curl.id,
        "name": curl.name,
        "timestamp": curl.timestamp.isoformat(),
        "description": curl.description,
        "command": curl.command
    }


def delete_all():
    return Curl.delete().execute()