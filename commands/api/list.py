from terminaltables import AsciiTable

from commands.base import CurlsCommand
from data.queries import api as aq


class APIListCommand(CurlsCommand):
    name = "api list"
    description = "List all curls associated with the current api."

    @classmethod
    def run(cls, args):
        api = aq.get_current()
        tabledata = []
        headers = ["id", "date", "command"]
        tabledata.append(headers)
        for curl in aq.get_curls(api):
            tabledata.append([
                curl.id,
                curl.timestamp,
                curl.command
            ])
        table_instance = AsciiTable(tabledata, api.name)
        print(table_instance.table)