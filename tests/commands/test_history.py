from src.data.queries import curl as cq
from src.commands.history import HistoryCommand


def test_history_command_no_history():
    result = HistoryCommand.run(['curls', 'history'])
    assert result.success

def test_history_command_with_history():
    curl = cq.save_history('curls google.com')
    result = HistoryCommand.run(['curls', 'history'])
    assert result.success
    assert "google.com" in result.output
    cq.delete(curl.id)

def test_history_command_help():
    curl = cq.save_history('curls google.com')
    result = HistoryCommand.run(['curls', 'history', 'help'])
    assert result.success
    assert "google.com" not in result.output
    cq.delete(curl.id)

