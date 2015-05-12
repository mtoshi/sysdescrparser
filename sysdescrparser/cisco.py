# -*- coding: utf-8 -*-

"""sysdescrparser.cisco."""

from sysdescr import SysDescr


# pylint: disable=no-name-in-module
class Cisco(SysDescr):

    """Class Cisco.

    This class is only for vendor definition.

    """

    def __init__(self, raw):
        """Constructor."""
        super(Cisco, self).__init__(raw)
        self.vendor = 'CISCO'
        self.model = self.UNKNOWN
        self.os = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        return self
