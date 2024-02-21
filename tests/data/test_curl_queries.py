from src.data.queries import curl as cq
from tests import clean_setup


@clean_setup
def test_save_history():
    curl = cq.save_history("curls google.com")
    curl2 = cq.get_by_id(curl.id)
    assert curl.command == curl2.command


@clean_setup
def test_add_metadata():
    curl = cq.save_history("curls google.com")
    NAME = "test-name"
    DESC = "this is a description"
    cq.add_metadata(curl.id, name=NAME, description=DESC)
    curl2 = cq.get_by_id(curl.id)
    assert curl2.name == NAME
    assert curl2.description == DESC


@clean_setup
def test_add_metadata_2():
    curl = cq.save_history("curls google.com")
    NAME = "test-name"
    DESC = "this is a description"
    cq.add_metadata(curl.id, name=None, description=DESC)
    curl2 = cq.get_by_id(curl.id)
    assert curl2.name == None
    assert curl2.description == DESC
    cq.add_metadata(curl.id, name=NAME, description=None)
    curl3 = cq.get_by_id(curl.id)
    assert curl3.name == NAME


@clean_setup
def test_get_history():
    curl = cq.save_history("curls google.com")
    curl2 = cq.save_history("curls yahoo.com")
    history = cq.get_history()
    assert len(history) == 2
    assert history[0].command == curl.command
    assert history[1].command == curl2.command
    cq.delete_all()
    history = cq.get_history()
    assert len(history) == 0


@clean_setup
def test_get_by_id():
    curl = cq.save_history("curls google.com")
    curl2 = cq.get_by_id(curl.id)
    assert curl.command == curl2.command
    cq.delete_all()
    curl2 = cq.get_by_id(curl.id)
    assert not curl2