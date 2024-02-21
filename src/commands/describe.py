from src.commands.base import CurlsCommand
from src.commands.result import command_result
from src.data.queries import curl as cq


class DescribeCommand(CurlsCommand):
    help_title = "Describe a curl."
    help_text = \
"""     $ curls describe
        * [curl_id] [new_description] - give a [new_description] description the curl [curl_id].
        * [-h|help] - show help
    """ 
    options = []

    @classmethod
    def run(cls, args):
        if len(args) == 3 and args[2] in ['-h', 'help']:
            return command_result(True, output=cls.help(args))
        if len(args) < 4:
            return command_result(False, output="curl_id and description required. Try 'curls describe help' for help.")
        description = args[3]
        curl_id = args[2]
        added = cq.add_metadata(curl_id, name=None, description=description)
        if not added:
            return command_result(False, output=f"Curl not found: '{curl_id}'.")
        return command_result(True, None, None)