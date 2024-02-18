from terminaltables import AsciiTable

from src.commands.base import CurlsCommand
from src.data.queries import curl as cq


class HistoryCommand(CurlsCommand):

    name = "history"
    description = "Show curls command history. All curls commands are stored by default."
    help_text = """
Show all curls history.
    $ curls history - show history of all curls, in chronological order, with the most recent at the bottom.
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
            return cls.help(args)
        curls = cq.get_history()
        tabledata = []
        headers = ["id", "date", "command"]
        tabledata.append(headers)
        for curl in curls:
            tabledata.append([
                curl.id,
                curl.timestamp,
                curl.command
            ])
        table_instance = AsciiTable(tabledata, "History")
        print(table_instance.table)
