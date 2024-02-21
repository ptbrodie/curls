from src.commands.base import CurlsCommand
from src.commands.api.add import APIAddCommand
from src.commands.api.delete import APIDeleteCommand
from src.commands.api.create import APICreateCommand
from src.commands.api.list import APIListCommand
from src.commands.api.remove import APIRemoveCommand
from src.commands.result import command_result
from src.commands import error
from src.data.queries import api as aq


class APICommand(CurlsCommand):
    help_title = "Manage an API."
    help_text = \
"""    $ curls api - list your APIs
        * [add] [curl_id] - add the given curl to the active API.
        * [remove] [curl_id] - delete the given curl from the active API.
        * [create] [api_name] - create a new API with the given name.
        * [delete] [api_name] - delete the given API.
        * [-h|help] - show help.
"""
    subcommands = {
        'add': APIAddCommand,
        'create': APICreateCommand,
        'delete': APIDeleteCommand,
        'remove': APIRemoveCommand,
        'list': APIListCommand,
    }

    @classmethod
    def run(cls, args):
        if (len(args) > 2) and (args[2] in ['-h', 'help']):
            return command_result(True, output=cls.help(args))
        if len(args) > 2:
            subcommand = args[2]
            if subcommand in cls.subcommands.keys():
                return cls.subcommands[subcommand].run(args)
            return command_result(False, output=f"Unknown subcommand: '{subcommand}'.")
        apis = aq.list_apis()
        current = sorted(apis, key=lambda a: a.date_current)[-1]
        result = ""
        count = 0
        for api in sorted(apis, key=lambda a: a.name):
            line = "  "
            if api.name == current.name:
                line = "* "
            line += api.name
            result += f"{line}"
            if count < len(apis) - 1:
                result += "\n"
            count += 1
        return command_result(True, output=result)
