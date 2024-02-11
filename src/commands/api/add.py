from src.commands.base import CurlsCommand
from src.data.queries import api as aq


class APIAddCommand(CurlsCommand):
    name = "api add [curl_id]"
    description = "Add a curl to an api by its id."

    @classmethod
    def run(cls, args):
        curr_api = aq.get_current()
        aq.add_to_api(curr_api, args[2])