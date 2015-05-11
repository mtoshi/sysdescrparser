# -*- coding: utf-8 -*-

"""sysdescrparser.a10."""

from sysdescr import SysDescr


# pylint: disable=no-name-in-module
class A10(SysDescr):

    """Class A10.

    This class is only for vendor definition.

    """

    def __init__(self, raw):
        """Constructor."""
        super(A10, self).__init__(raw)
        self.vendor = 'A10'
        self.model = self.UNKNOWN
        self.os = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        return self
