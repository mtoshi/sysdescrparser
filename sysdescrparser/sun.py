# -*- coding: utf-8 -*-

"""sysdescrparser.sun."""

from sysdescr import SysDescr


# pylint: disable=no-name-in-module
class Sun(SysDescr):

    """Class Sun.

    This class is only for vendor definition.

    """

    def __init__(self, raw):
        """Constructor."""
        super(Sun, self).__init__(raw)
        self.vendor = 'SUN'
        self.model = self.UNKNOWN
        self.os = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        return self
