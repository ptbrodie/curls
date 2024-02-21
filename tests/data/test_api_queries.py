import pytest

from src.data.queries import api as aq, curl as cq
from tests import clean_setup


@clean_setup
def test_new_api_success():
    API_NAME = "test-api"
    api = aq.new_api(API_NAME)
    api2 = aq.get_by_id(api.id)
    assert api2.name == API_NAME


@clean_setup
def test_new_api_duplicate():
    API_NAME = "test-api"
    aq.new_api(API_NAME)
    api2 = aq.new_api(API_NAME)
    assert not api2


@clean_setup
def test_new_api_invalid_name():
    API_NAME = "test api"
    with pytest.raises(Exception):
        aq.new_api(API_NAME)


@clean_setup
def test_get_current():
    API_NAME = "test-api"
    api = aq.new_api(API_NAME)
    aq.set_current(api.name)
    api2 = aq.get_current()
    assert api2.name == API_NAME


@clean_setup
def test_add_to_api_remove_from_api_success():
    curl = cq.save_history("curls google.com")
    API_NAME = "test-api"
    api = aq.new_api(API_NAME)
    aq.add_to_api(api, curl.id)
    curls = aq.get_curls(api)
    found = False
    for c in curls:
        if c.id == curl.id:
            found = True
            break
    assert found
    aq.remove_from_api(api, curl.id)
    curls = aq.get_curls(api)
    found = False
    for c in curls:
        if c.id == curl.id:
            found = True
            break
    assert not found