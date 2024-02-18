import json
import re
from uuid import uuid4

from src.commands.base import CurlsCommand
from src.data.queries import api as aq, curl as cq


class ImportCommand(CurlsCommand):
    name = "import [file_name]"
    description = "Import an api from the given [filename]."
    help_text = """
Import an API from a json file.
    $ curls import
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
            print("Filename required. Try 'curls import help' for help.")
            return False
        api_name = None
        filename = args[2]
        if args[2] in ['-n', '--name']:
            api_name = args[3]
            filename = args[4]
        with open(filename, "r") as f:
            content = json.load(f)
            uu = str(uuid4())
            name = api_name if api_name else f"{content['name']}-{uu[:8]}"
            api = aq.new_api(name)
            api.date_created = content["date_created"]
            for curl_data in content["curls"]:
                curl = cq.new_curl(curl_data["command"], curl_data["timestamp"])
                aq.add_to_api(api, curl.id)
            print(f"Imported API '{api.name}")
            return True