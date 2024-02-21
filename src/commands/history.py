from terminaltables import AsciiTable

from src.commands.base import CurlsCommand
from src.commands.result import command_result
from src.data.queries import curl as cq
from src.formatting import text


class HistoryCommand(CurlsCommand):

    help_title = "Show all curls history."
    help_text = \
"""     $ curls history - show history of all curls, in chronological order, with the most recent at the bottom.
        * [-h|help] - show help
"""
    subcommands = {}

    @classmethod
    def get_description(cls):
        return cls.description

    @classmethod
    def get_name(cls):
        return cls.name

    @classmethod
    def get_subcommands(cls):
        return cls.subcommands

    @classmethod
    def run(cls, args):
        if len(args) > 2 and args[2] in ['-h', 'help']:
            return command_result(True, output=cls.help(args))
        curls = cq.get_history()
        tabledata = []
        headers = ["id", "name", "date", "command"]
        tabledata.append(headers)
        for curl in curls:
            tabledata.append([
                curl.id,
                curl.name or "-",
                curl.timestamp,
                f"$ {text.wrapped_text(curl.command)}"
            ])
        table_instance = AsciiTable(tabledata, "History")
        return command_result(success=True, output=table_instance.table, errors=[])
