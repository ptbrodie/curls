from src.commands.base import CurlsCommand
from src.data.queries import curl as cq
from src.commands.result import command_result


class DeleteCommand(CurlsCommand):
    help_title = "Delete a curl."
    help_text = \
"""     $ curls delete
        * [curl_id] - delete the given curl by its id.
        * [curl_name] - delete the give curl by its name [must name it first].
        * [-h|help] - show help
    """ 
    options = []


    @classmethod
    def run(cls, args):
        if len(args) < 3:
            return command_result(False, output="curl_id or curl_name required. Try 'curls delete help' for help.", errors=None)
        curl_arg = args[2]
        curl = cq.get_by_id(curl_arg)
        if curl:
            cq.delete(curl.id)
            return command_result(True, output=None, errors=None)
        curl = cq.get_by_name(curl_arg)
        if curl:
            cq.delete(curl.id)
            return command_result(True, output=None, errors=None)
        return command_result(False, output=f"curl '{curl_arg}' not found. Try 'curls delete help' for help.", errors=None)
