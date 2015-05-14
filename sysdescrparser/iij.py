# -*- coding: utf-8 -*-

"""sysdescrparser.iij."""

from sysdescr import SysDescr


# pylint: disable=no-name-in-module
class IIJ(SysDescr):

    """Class IIJ.

    This class is only for vendor definition.

    """

    def __init__(self, raw):
        """Constructor."""
        super(IIJ, self).__init__(raw)
        self.vendor = 'IIJ'
        self.model = self.UNKNOWN
        self.os = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        return self
