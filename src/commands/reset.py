import shutil

from src.commands.base import CurlsCommand
from src.commands.result import command_result
import src.data as data


class ResetCommand(CurlsCommand):
    subcommands = {}
    help_title = "Reset curls."
    help_text = \
"""     $ curls reset - delete all curls, and all apis.
        * WARNING: This cannot be undone.
"""

    @classmethod
    def run(cls, args):
        shutil.rmtree(data.CURLSDIR)
        return command_result(success=True, output="All curls and apis have been deleted.", errors=[])
