from commands.base import CurlsCommand
from data.queries import api as aq


class UseCommand(CurlsCommand):
    name = "use [api_name]"
    description = "Switch to the given api [api_name]"
    subcommands = {}

    @classmethod
    def run(cls, args):
        name = args[2]
        found = aq.set_current(name)
        if not found:
            raise Exception(f"API not found: '{name}'.")