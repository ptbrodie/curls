from termcolor import colored

class CurlsCommand():
    help_title = "Title goes here."
    help_text = "No help text provided."
    subcommands = {}

    @classmethod
    def get_subcommands(cls):
        return cls.subcommands

    @classmethod
    def run(cls, args):
        raise NotImplementedError()

    @classmethod
    def help(cls, args):
        result = "\n"
        result += colored(cls.help_title, None, None, attrs=['bold'])
        result += "\n"
        result += cls.help_text
        return result