from terminaltables import AsciiTable

from commands.base import CurlsCommand
from data.queries import curl as cq


class HistoryCommand(CurlsCommand):

    name = "history"
    description = "Show curls command history. All curls commands are stored by default."
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

    @staticmethod
    def run(args):
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
