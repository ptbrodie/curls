from src.commands.api import APICommand
from src.commands.base import CurlsCommand
from src.commands.export import ExportCommand
from src.commands.history import HistoryCommand
from src.commands.imp import ImportCommand
from src.commands.reset import ResetCommand
from src.commands.use import UseCommand


class HelpCommand(CurlsCommand):
    name = "help"
    description = "Display help for commands."
    subcommands = {}
    commands = [
        APICommand,
        UseCommand,
        ExportCommand,
        ImportCommand,
        HistoryCommand,
        ResetCommand,
    ]

    @classmethod
    def run(cls, args):
        for command in cls.commands:
            command.help(args)
        return True

