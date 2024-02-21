from src.commands.name import NameCommand
from src.data.queries import curl as cq
from tests import clean_setup


@clean_setup
def test_name_command_no_name():
    result = NameCommand.run(['curls', 'name'])
    assert not result.success


@clean_setup
def test_name_command_help():
    result = NameCommand.run(['curls', 'name', 'help'])
    assert result.success
    assert NameCommand.help_title in result.output


@clean_setup
def test_name_command_success():
    curl = cq.save_history('curls google.com')
    result = NameCommand.run(['curls', 'name', curl.id, 'test-name'])
    assert result.success
    cq.get_by_id(curl.id).name == 'test-name'
    cq.delete(curl.id)


@clean_setup
def test_name_command_success_with_description():
    curl = cq.save_history('curls google.com')
    result = NameCommand.run(['curls', 'name', curl.id, 'test-name', '-d', 'test-description'])
    assert result.success
    curl = cq.get_by_id(curl.id)
    assert curl.name == 'test-name'
    assert curl.description == 'test-description'
    cq.delete(curl.id)


@clean_setup
def test_name_command_not_found():
    result = NameCommand.run(['curls', 'name', 'not-found', 'test-name'])
    assert not result.success
    assert "Curl not found" in result.output