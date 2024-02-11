class CommandNotFoundError(Exception):
    def __init__(self, args):
        self.message = f"'{' '.join(args)}' not found"
        