# -*- coding: utf-8 -*-

"""sysdescrparser.foundry."""

from sysdescr import SysDescr


# pylint: disable=no-name-in-module
class Foundry(SysDescr):

    """Class Foundry.

    This class is only for vendor definition.

    """

    def __init__(self, raw):
        """Constructor."""
        super(Foundry, self).__init__(raw)
        self.vendor = 'FOUNDRY'
        self.model = self.UNKNOWN
        self.os = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        return self
