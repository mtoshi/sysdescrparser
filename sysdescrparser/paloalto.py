# -*- coding: utf-8 -*-

"""sysdescrparser.paloalto."""

from sysdescr import SysDescr


# pylint: disable=no-name-in-module
class PaloAlto(SysDescr):

    """Class PaloAlto.

    This class is only for vendor definition.

    """

    def __init__(self, raw):
        """Constructor."""
        super(PaloAlto, self).__init__(raw)
        self.vendor = 'PALOALTO'
        self.model = self.UNKNOWN
        self.os = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        return self
