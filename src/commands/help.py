from src.commands.api import APICommand
from src.commands.base import CurlsCommand
from src.commands.export import ExportCommand
from src.commands.history import HistoryCommand
from src.commands.imp import ImportCommand
from src.commands.reset import ResetCommand
from src.commands.result import command_result
from src.commands.use import UseCommand


class HelpCommand(CurlsCommand):
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
        output = ""
        for command in cls.commands:
            output += command.help(args)
        return command_result(True, output, None)

