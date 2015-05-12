# -*- coding: utf-8 -*-

"""sysdescrparser.juniper."""

from sysdescr import SysDescr


# pylint: disable=no-name-in-module
class Juniper(SysDescr):

    """Class Juniper.

    This class is only for vendor definition.

    """

    def __init__(self, raw):
        """Constructor."""
        super(Juniper, self).__init__(raw)
        self.vendor = 'JUNIPER'
        self.model = self.UNKNOWN
        self.os = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        return self
