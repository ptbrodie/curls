from src.commands.base import CurlsCommand
from src.data.queries import api as aq
from src.commands.result import command_result


def new_api(args):
    return aq.new_api(args[3])

class UseCommand(CurlsCommand):
    subcommands = {}
    help_title = "Choose which API to use."
    help_text = \
"""     $ curls use
        * [api_name] - switch to using the given existing api_name
        * [-n|--name] [api_name] - create new API with the given api_name and switch to use it.
        * [-h|help] - show help
    """ 
    options = {
        '-n': new_api,
        '--name': new_api,
    }

    @classmethod
    def run(cls, args):
        if len(args) < 3 or args[2] in ['-h', 'help']:
            return command_result(True, output=cls.help(args), errors=None)
        next = args[2]
        if next in cls.options.keys():
            api = cls.options[next](args)
            aq.set_current(api.name)
            return command_result(True, None, None)
        found = aq.set_current(next)
        if not found:
            return command_result(False, output=f"API not found: '{next}'.")
        return command_result(True, None, None)