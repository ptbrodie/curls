from commands.base import CurlsCommand


class APIHelpCommand(CurlsCommand):
    name = "api help [curl_id]"
    description = "Display help for api commands"
    options = []

    @classmethod
    def run(cls, args):
        print("api help command")