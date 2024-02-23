import json
import os
import re
from uuid import uuid4

from src.commands.base import CurlsCommand
from src.commands.result import command_result
from src.data.queries import api as aq, curl as cq


class ImportCommand(CurlsCommand):
    help_title = "Import an API from a json file."
    help_text = \
"""     $ curls import
        * [filename] - import an api from the given [filename].
        * [-n|--name] [api_name] [filename] - import an api from the given [filename] and name it [api_name].
        * [-h|help] - show help
    """ 
    options = []

    @classmethod
    def validate_name(cls, name):
        if re.match(r'.*\s.*', name):
            raise Exception('Name invalid: spaces not allowed')
        return True

    @classmethod
    def run(cls, args):
        if len(args) < 3:
            return command_result(False, output="Filename required. Try 'curls import help' for help.")
        if args[2] in ['-h', 'help']:
            return command_result(True, output=cls.help(args))
        api_name = None
        filename = args[2]
        if args[2] in ['-n', '--name']:
            api_name = args[3]
            filename = args[4]
        if not os.path.exists(filename):
            return command_result(False, output=f"File not found: '{filename}'.")
        with open(filename, "r") as f:
            content = json.load(f)
            uu = str(uuid4())
            name = api_name if api_name else f"{content['name']}-{uu[:8]}"
            api = aq.new_api(name)
            api.date_created = content["date_created"]
            for curl_data in content["curls"]:
                curl = cq.from_json(curl_data)
                aq.add_to_api(api, curl.id)
            return command_result(True, output=f"Imported API '{api.name}' from '{filename}'.")