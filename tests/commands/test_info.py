from src.commands.info import InfoCommand
from src.data.queries import curl as cq
from tests import clean_setup


@clean_setup
def test_info_command_no_args():
    result = InfoCommand.run(['curls', 'info'])
    assert not result.success


@clean_setup
def test_info_command_help():
    result = InfoCommand.run(['curls', 'info', 'help'])
    assert result.success
    assert InfoCommand.help_title in result.output


@clean_setup
def test_info_command_success():
    curl = cq.save_history('curls google.com')
    result = InfoCommand.run(['curls', 'info', curl.id])
    assert result.success
    assert "google.com" in result.output
    cq.delete(curl.id)


@clean_setup
def test_info_command_not_found():
    result = InfoCommand.run(['curls', 'info', 'not-found'])
    assert not result.success
    assert "Curl not found" in result.output