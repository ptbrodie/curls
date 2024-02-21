from src.commands.base import CurlsCommand
from src.commands.result import command_result
from src.data.queries import curl as cq


class NameCommand(CurlsCommand):
    help_title = "Name a curl."
    help_text = \
"""     $ curls name
        * [curl_id] [new_name] - give a [new_name] name the curl [curl_id].
        * [curl_id] [new_name] [-d|--describe|--description] [new_description] - give a [new_name] name to the curl [curl_id], and add a description.
        * [-h|help] - show help
    """ 
    options = []

    @classmethod
    def run(cls, args):
        if len(args) == 3 and args[2] in ['-h', 'help']:
            return command_result(True, cls.help(args))
        if len(args) < 4:
            return command_result(False, output="curl_id and name required. Try 'curls name help' for help.")
        curl_name = args[3]
        curl_id = args[2]
        description = None
        if len(args) > 5 and args[4] in ['-d', '--describe', '--description']:
            description = args[5]
        curl = cq.add_metadata(curl_id, name=curl_name, description=description)
        if not curl:
            return command_result(False, output=f"Curl not found: '{curl_id}'.")
        return command_result(True, None, None)