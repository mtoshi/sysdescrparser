# -*- coding: utf-8 -*-

"""sysdescrparser.hp."""

from sysdescr import SysDescr


# pylint: disable=no-name-in-module
class HP(SysDescr):

    """Class HP.

    This class is only for vendor definition.

    """

    def __init__(self, raw):
        """Constructor."""
        super(HP, self).__init__(raw)
        self.vendor = 'HP'
        self.model = self.UNKNOWN
        self.os = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        return self
