# -*- coding: utf-8 -*-

"""sysdescrparser.FortiNet."""

from sysdescrparser.sysdescr import SysDescr


# pylint: disable=no-name-in-module
class FortiNet(SysDescr):

    """Class FortiNet.

    This class is only for vendor definition.

    """

    def __init__(self, raw):
        """Constructor."""
        super(FortiNet, self).__init__(raw)
        self.vendor = 'fortinet'
        self.model = self.UNKNOWN
        self.os = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        return self
