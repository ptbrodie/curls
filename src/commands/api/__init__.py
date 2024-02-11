from src.commands.base import CurlsCommand
from src.commands.api.add import APIAddCommand
from src.commands.api.delete import APIDeleteCommand
from src.commands.api.help import APIHelpCommand
from src.commands.api.create import APICreateCommand
from src.commands.api.list import APIListCommand
from src.commands import error
from src.data.queries import api as aq


class APICommand(CurlsCommand):
    name = "api"
    description = "Commands to run on api of curls."
    subcommands = {
        'add': APIAddCommand,
        'create': APICreateCommand,
        'del': APIDeleteCommand,
        'delete': APIDeleteCommand,
        'remove': APIDeleteCommand,
        'help': APIHelpCommand,
        'list': APIListCommand,
    }

    @classmethod
    def run(cls, args):
        if len(args) > 2:
            subcommand = args[2]
            if subcommand in cls.subcommands.keys():
                return cls.subcommands[subcommand].run(args)
            raise error.CommandNotFoundError(args)
        apis = aq.list_apis()
        current = sorted(apis, key=lambda a: a.date_current)[-1]
        for api in sorted(apis, key=lambda a: a.name):
            line = "  "
            if api.name == current.name:
                line = "* "
            line += api.name
            print(line)
