import re

from src.commands.base import CurlsCommand
from src.commands.result import command_result
from src.data.queries import api as aq


class APICreateCommand(CurlsCommand):
    options = []

    @classmethod
    def validate_name(cls, name):
        return not re.match(r'.*\s.*', name)

    @classmethod
    def run(cls, args):
        name = args[3]
        valid = cls.validate_name(name)
        if not valid:
            return command_result(False, output="Name invalid: spaces not allowed" )
        api = aq.new_api(name)
        if not api:
            return command_result(False, output=f"API already exists: '{name}'.")
        return command_result(True, None, None)