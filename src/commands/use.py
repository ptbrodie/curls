from src.commands.base import CurlsCommand
from src.data.queries import api as aq

def new_api(args):
    return aq.new_api(args[3])

class UseCommand(CurlsCommand):
    name = "use [api_name]"
    description = "Switch to the given api [api_name]"
    subcommands = {}
    help_text = """
Choose which API to use.
    $ curls use
        * [api_name] - switch to using the given existing api_name
        * [-n] [api_name] - create new API with the given api_name and switch to use it.
        * [-h|help] - show help
    """ 
    options = {
        '-n': new_api,
    }

    @classmethod
    def run(cls, args):
        if len(args) < 3:
            cls.help(args)
        next = args[2]
        if next in ['-h', 'help']:
            return cls.help(args)
        if next in cls.options.keys():
            api = cls.options[next](args)
            aq.set_current(api.name)
            return True
        found = aq.set_current(next)
        if not found:
            raise Exception(f"API not found: '{name}'.")
        return True