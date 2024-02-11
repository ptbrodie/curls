import shutil

from commands.base import CurlsCommand
import data


class ResetCommand(CurlsCommand):
    name = "reset"
    description = "Reset your curls history. Delete all saved curls."
    subcommands = {}

    @classmethod
    def run(cls, args):
        shutil.rmtree(data.CURLSDIR)
        print("Done resetting.")
