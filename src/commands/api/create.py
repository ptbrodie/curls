import re

from src.commands.base import CurlsCommand
from src.data.queries import api as aq


class APICreateCommand(CurlsCommand):
    name = "api create [api_name]"
    description = "Create a new api with the given [api_name]."
    options = []

    @classmethod
    def validate_name(cls, name):
        if re.match(r'.*\s.*', name):
            raise Exception('Name invalid: spaces not allowed')
        return True

    @classmethod
    def run(cls, args):
        name = args[3]
        cls.validate_name(name)
        aq.new_api(name)