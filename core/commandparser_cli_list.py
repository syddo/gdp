'''
            GDP - The Generic Device Programmer.

    By Dean Camera (dean [at] fourwalledcubicle [dot] com)

   Release under a MIT license; see LICENSE.txt for details.
'''

from optparse import OptionParser

from core.util import *
from core.commandparser import *
from tools import *


class CommandParserCLIList(CommandParser):
    def _parser_error(self, message):
        raise CommandParserError("LIST", message)


    def _show_connected_tools(self):
        print("Currently connected USB tools:")

        for tool in Util.get_subclasses(Tool):
            tool_name = tool.get_name()

            for serial in set(tool.find_connected()):
                print("  - %s, serial number %s" % (tool_name, serial))


    def parse_arguments(self, args):
        description = "LIST command: lists currently connected USB tools."

        parser = OptionParser(description=description, usage="")
        parser.error = self._parser_error
        parser.disable_interspersed_args()

        (self.options, args) = parser.parse_args(args=args)

        self._show_connected_tools()

        return args


    def can_execute(self):
        return False


    def execute(self, session):
        pass
