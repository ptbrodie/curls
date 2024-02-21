from src.commands.use import UseCommand
from src.data.queries import api as aq


def test_use_command_no_args():
    result = UseCommand.run(['curls', 'use'])
    assert result.success
    assert UseCommand.help_title in result.output


def test_use_command_help():
    result = UseCommand.run(['curls', 'use', 'help'])
    assert result.success
    assert UseCommand.help_title in result.output


def test_use_command_new_api():
    result = UseCommand.run(['curls', 'use', '-n', 'new_api'])
    assert result.success
    api = aq.get_current()
    assert api.name == "new_api"
    aq.delete(api.id)


def test_use_existing_api():
    aq.new_api("test-api")
    result = UseCommand.run(['curls', 'use', 'test-api'])
    assert result.success
    api = aq.get_current()
    assert api.name == "test-api"
    aq.delete(api.id)
