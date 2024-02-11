from src.commands.base import CurlsCommand
from src.data.queries import api as aq


class APIDeleteCommand(CurlsCommand):
    name = "api delete [curl_id]"
    description = "Delete a curl from an api by its id."

    @classmethod
    def run(cls, args):
        curr_api = aq.get_current()
        aq.delete_from_api(curr_api, args[2])