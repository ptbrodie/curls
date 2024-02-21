from datetime import datetime

from src.commands.describe import DescribeCommand
from src.data.queries import curl as cq


def test_describe_command_no_description():
    result = DescribeCommand.run(['curls', 'describe'])
    assert not result.success


def test_describe_command_help():
    result = DescribeCommand.run(['curls', 'describe', 'help'])
    assert result.success
    assert DescribeCommand.help_title in result.output


def test_describe_command_success():
    curl = cq.save_history('curls google.com')
    result = DescribeCommand.run(['curls', 'describe', curl.id, 'test-description'])
    assert result.success
    assert result.output is None
    curl = cq.get_by_id(curl.id)
    assert curl.description == 'test-description'
    cq.delete(curl.id)


def test_description_command_not_found():
    result = DescribeCommand.run(['curls', 'describe', 'not-found', 'test-description'])
    assert not result.success
    assert "Curl not found" in result.output