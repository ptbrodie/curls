import shutil

from src.commands.base import CurlsCommand
import src.data as data


class ResetCommand(CurlsCommand):
    name = "reset"
    description = "Reset your curls history. Delete all saved curls."
    subcommands = {}

    @classmethod
    def run(cls, args):
        shutil.rmtree(data.CURLSDIR)
        print("Done resetting.")
