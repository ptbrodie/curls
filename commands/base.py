

class CurlsCommand():
    name = "No command name"
    description = "No description provided"
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