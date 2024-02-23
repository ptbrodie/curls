import os

from src.commands.export import ExportCommand
from src.commands.imp import ImportCommand
from src.data.queries import api as aq, curl as cq
from tests import clean_setup


@clean_setup
def test_import_command_no_file():
    result = ImportCommand.run(['curls', 'import'])
    assert not result.success


@clean_setup
def test_import_command_help():
    result = ImportCommand.run(['curls', 'import', 'help'])
    assert result.success
    assert ImportCommand.help_title in result.output


@clean_setup
def test_import_command_success():
    api = aq.new_api('test-import')
    curl = cq.save_history("curls google.com")
    cq.add_metadata(curl.id, name="test-curl")
    aq.add_to_api(api, curl.id)
    curl = cq.get_by_id(curl.id)
    ExportCommand.run(['curls', 'export', 'test-import'])
    aq.delete(api.id)
    cq.delete_all()
    result = ImportCommand.run(['curls', 'import', 'test-import.json'])
    assert result.success
    assert "test-import" in result.output
    apis = aq.list_apis()
    found = None
    for api in apis:
        if "test-import" in api.name:
            found = api
            break
    assert found
    assert len(aq.get_curls(found)) == 1
    curl_found = None
    for c in aq.get_curls(found):
        if c.name == curl.name:
            curl_found = c
            break
    assert curl_found
    os.remove('test-import.json')


@clean_setup
def test_import_command_file_not_found():
    result = ImportCommand.run(['curls', 'import', 'not-found.json'])
    assert not result.success
    assert "File not found" in result.output