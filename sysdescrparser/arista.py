# -*- coding: utf-8 -*-

"""sysdescrparser.arista."""

from sysdescr import SysDescr


# pylint: disable=no-name-in-module
class Arista(SysDescr):

    """Class Arista.

    This class is only for vendor definition.

    """

    def __init__(self, raw):
        """Constructor."""
        super(Arista, self).__init__(raw)
        self.vendor = 'ARISTA'
        self.model = self.UNKNOWN
        self.os = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        return self
