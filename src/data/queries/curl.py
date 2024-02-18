from uuid import uuid4 

from src.data.models.curl import Curl


def get_by_id(id):
    return Curl.get_by_id(id)


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


def to_json(curl):
    return {
        "id": curl.id,
        "timestamp": curl.timestamp.isoformat(),
        "command": curl.command
    }
