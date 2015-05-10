# -*- coding: utf-8 -*-

"""sysdescrparser.citrix."""

from sysdescr import SysDescr


# pylint: disable=no-name-in-module
class Citrix(SysDescr):

    """Class Citrix.

    This class is only for vendor definition.

    """

    def __init__(self, raw):
        """Constructor."""
        super(Citrix, self).__init__(raw)
        self.vendor = 'CITRIX'
        self.model = self.UNKNOWN
        self.os = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        return self
