from terminaltables import AsciiTable

from src.commands.base import CurlsCommand
from src.commands.result import command_result
from src.data.queries import api as aq
from src.formatting import text


class APIListCommand(CurlsCommand):

    @classmethod
    def run(cls, args):
        api = aq.get_current()
        tabledata = []
        headers = ["id", "name", "date", "command"]
        tabledata.append(headers)
        for curl in aq.get_curls(api):
            tabledata.append([
                curl.id,
                curl.name or "-",
                curl.timestamp,
                text.wrapped_text(curl.command)
            ])
        table_instance = AsciiTable(tabledata, api.name)
        return command_result(True, table_instance.table)