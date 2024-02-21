from src.commands.api import APICommand, APIAddCommand, APIRemoveCommand
from src.data.queries import api as aq, curl as cq
from tests import clean_setup

@clean_setup
def test_api_command_no_args():
    result = APICommand.run(['curls', 'api'])
    assert result.success
    assert "default" in result.output


@clean_setup
def test_api_command_help():
    result = APICommand.run(['curls', 'api', 'help'])
    assert result.success
    assert APICommand.help_title in result.output


@clean_setup
def test_api_command_create_delete():
    name = "test-api-command-create-delete"
    result = APICommand.run(['curls', 'api', 'create', name])
    assert result.success
    assert not result.output
    result = APICommand.run(['curls', 'api'])
    assert result.success
    assert name in result.output
    result = APICommand.run(['curls', 'api', 'delete', name])
    assert result.success
    result = APICommand.run(['curls', 'api'])
    assert result.success
    assert name not in result.output
    curl = aq.get_by_name(name)
    assert not curl


@clean_setup
def test_api_command_create_duplicate():
    name = "test-api-command-create-duplicate"
    result = APICommand.run(['curls', 'api', 'create', name])
    assert result.success
    assert not result.output
    result = APICommand.run(['curls', 'api', 'create', name])
    assert not result.success
    assert "API already exists" in result.output
    result = APICommand.run(['curls', 'api', 'delete', name])
    assert result.success
    curl = aq.get_by_name(name)
    assert not curl


@clean_setup
def test_api_command_create_invalid_name():
    name = "test api command create invalid name"
    result = APICommand.run(['curls', 'api', 'create', name])
    assert not result.success
    assert "Name invalid" in result.output
    curl = aq.get_by_name(name)
    assert not curl


@clean_setup
def test_api_command_delete_not_found():
    name = "test-api-command-delete-not-found"
    result = APICommand.run(['curls', 'api', 'delete', name])
    assert not result.success
    assert "API not found" in result.output
    curl = aq.get_by_name(name)
    assert not curl


@clean_setup
def test_api_add_remove_curl():
    cq.delete_all()
    aq.delete_all()
    curl = cq.save_history('curls google.com')
    api = aq.new_api('test-api-add-remove-curl')
    aq.set_current(api.name)
    api = aq.get_current()
    curl = cq.get_by_id(curl.id)
    assert api.name == 'test-api-add-remove-curl'
    result = APICommand.run(['curls', 'api', 'add', curl.id])
    assert result.success
    assert len(aq.get_curls(api)) == 1
    result = APICommand.run(['curls', 'api', 'remove', curl.id])
    assert result.success
    assert len(aq.get_curls(api)) == 0
    aq.delete(api.id)
    cq.delete(curl.id)


@clean_setup
def test_api_add_remove_curl_2():
    cq.delete_all()
    aq.delete_all()
    curl = cq.save_history('curls google.com')
    api = aq.new_api('test-api-add-remove-curl-2')
    aq.set_current(api.name)
    api = aq.get_current()
    curl = cq.get_by_id(curl.id)
    assert api.name == 'test-api-add-remove-curl-2'
    result = APIAddCommand.run(['curls', 'add', curl.id])
    assert result.success
    assert len(aq.get_curls(api)) == 1
    result = APIRemoveCommand.run(['curls', 'remove', curl.id])
    assert result.success
    assert len(aq.get_curls(api)) == 0
    aq.delete(api.id)
    cq.delete(curl.id)