from commands.base import CurlsCommand


class HelpCommand(CurlsCommand):
    name = "help"
    description = "Display help for commands."
    subcommands = {}

    @classmethod
    def run(cls, args):
        print("HELP COMMAND")
        print("TODO: update help to print out the commands and their descriptions")
        print("TODO: error handling should log the entire command")
        print("TODO: show tree and subtree of commands when help called")
        print("TODO: add options to commands")
        print("Commands:")
        print("  - api")
        print("  - history")
        print("  - reset")

