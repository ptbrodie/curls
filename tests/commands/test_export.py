import os

from src.commands.export import ExportCommand
from src.data.queries import api as aq
from tests import clean_setup


@clean_setup
def test_export_command_no_name():
    result = ExportCommand.run(['curls', 'export'])
    assert not result.success


@clean_setup
def test_export_command_help():
    result = ExportCommand.run(['curls', 'export', 'help'])
    assert result.success
    assert ExportCommand.help_title in result.output


@clean_setup
def test_export_command_success():
    api = aq.new_api('test-export')
    result = ExportCommand.run(['curls', 'export', 'test-export'])
    assert result.success
    assert f"{api.name}.json" in result.output
    os.remove(f"{api.name}.json")


@clean_setup
def test_export_command_not_found():
    result = ExportCommand.run(['curls', 'export', 'not-found'])
    assert not result.success
    assert "API not found" in result.output


@clean_setup
def test_export_command_with_filename():
    api = aq.new_api('test-export')
    result = ExportCommand.run(['curls', 'export', 'test-export', '-f', 'test-filename'])
    assert result.success
    assert "test-filename" in result.output
    os.remove("test-filename")