class CommandResult:
    def __init__(self, success, output=None, errors=None):
        self.success = success
        self.output = output
        self.errors = errors or []


def command_result(success, output=None, errors=None):
    return CommandResult(success, output, errors)