from termcolor import colored

from src.commands.base import CurlsCommand
from src.commands.result import command_result
from src.data.queries import curl as cq
from src.formatting import text

class InfoCommand(CurlsCommand):
    help_title = "Get info about a curl."
    help_text = \
"""     $ curls info
        * [curl_id] - get info about the curl [curl_id].
        * [-h|help] - show help
"""
    options = []

    @classmethod
    def run(cls, args):
        if len(args) < 3:
            return command_result(False, output="curl_id required. Try 'curls info help' for help.")
        if args[2] in ['-h', 'help']:
            return command_result(True, cls.help(args))
        curl = cq.get_by_identifier(args[2])
        if not curl:
            return command_result(False, output=f"Curl not found: '{args[2]}'.")
        result = "\n"
        result += f"{colored('ID:', None, None, attrs=['bold'])} {curl.id}\n"
        result += f"{colored('Date:', None, None, attrs=['bold'])} {curl.timestamp}\n"
        result += f"{colored('Name:', None, None, attrs=['bold'])} {curl.name or 'No name provided.'}\n"
        result += f"{colored('Description:', None, None, attrs=['bold'])} {text.wrapped_text(curl.description or 'No description provided.')}\n"
        result += f"{colored('Command:', None, None, attrs=['bold'])} {text.wrapped_text(curl.command)}\n"
        result += "\n"
        return command_result(True, output=result, errors=[])