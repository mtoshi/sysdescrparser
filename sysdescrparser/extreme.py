# -*- coding: utf-8 -*-

"""sysdescrparser.extreme."""

from sysdescr import SysDescr


# pylint: disable=no-name-in-module
class Extreme(SysDescr):

    """Class Extreme.

    This class is only for vendor definition.

    """

    def __init__(self, raw):
        """Constructor."""
        super(Extreme, self).__init__(raw)
        self.vendor = 'EXTREME'
        self.model = self.UNKNOWN
        self.os = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        return self
