from src.commands.base import CurlsCommand
from src.commands.result import command_result
from src.data.queries import api as aq


class APIDeleteCommand(CurlsCommand):
    options = []

    @classmethod
    def run(cls, args):
        name = args[3]
        api = aq.get_by_name(name)
        if not api:
            return command_result(False, output=f"API not found: '{name}'.")
        aq.delete(api.id)
        return command_result(True, None, None)