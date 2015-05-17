# -*- coding: utf-8 -*-

"""sysdescrparser.yamaha."""

from sysdescr import SysDescr


# pylint: disable=no-name-in-module
class Yamaha(SysDescr):

    """Class Yamaha.

    This class is only for vendor definition.

    """

    def __init__(self, raw):
        """Constructor."""
        super(Yamaha, self).__init__(raw)
        self.vendor = 'YAMAHA'
        self.model = self.UNKNOWN
        self.os = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        return self
