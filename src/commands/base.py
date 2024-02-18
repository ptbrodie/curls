

class CurlsCommand():
    name = "No command name"
    description = "No description provided"
    help_text = "No help text provided."
    subcommands = {}

    @classmethod
    def get_description(cls):
        return cls.description

    @classmethod
    def get_name(cls):
        return cls.name

    @classmethod
    def get_subcommands(cls):
        return cls.subcommands

    @classmethod
    def run(cls, args):
        raise NotImplementedError()

    @classmethod
    def help(cls, args):
        print(cls.help_text)
        return True