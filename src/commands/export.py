import json
import re

from src.commands.base import CurlsCommand
from src.commands.result import command_result
from src.data.queries import api as aq

class ExportCommand(CurlsCommand):
    help_title = "Export an API to a file."
    help_text = \
"""     $ curls export
        * [api_name] - export the given api to a file [api_name].json
        * [api_name] [-f|--filename] [filename] - export the given api to a file [filename].json
        * [-h|help] - show help
    """ 
    options = { }


    @classmethod
    def validate_name(cls, name):
        if re.match(r'.*\s.*', name):
            raise Exception('Name invalid: spaces not allowed')
        return True


    @classmethod
    def run(cls, args):
        if len(args) < 3:
            return command_result(False, output="API name required. Try 'curls export help' for help.")
        api_name = args[2]
        if api_name in ['-h', 'help']:
            return command_result(True, output=cls.help(args))
        filename = f"{api_name}.json"
        if len(args) > 3 and args[3] in ['-f', '--filename']:
            filename = args[4]
        api = aq.get_by_name(api_name)
        if not api:
            return command_result(False, output=f"API not found: '{api_name}'.")
        api_json = aq.to_json(api)
        with open(filename, "w") as f:
            json.dump(api_json, f)
        return command_result(True, output=f"Saved API to '{filename}'")