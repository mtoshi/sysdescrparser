# -*- coding: utf-8 -*-

"""sysdescrparser.linux."""

import re
from sysdescr import SysDescr


# pylint: disable=no-name-in-module
# pylint: disable=no-member
class Linux(SysDescr):

    """Class Linux.

    This class is only for vendor definition.

    """

    def __init__(self, raw):
        """Constructor."""
        super(Linux, self).__init__(raw)
        self.vendor = self.UNKNOWN
        self.model = self.UNKNOWN
        self.os = 'LINUX'
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        regex = (r'^Linux\s+')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            regex = (r'\s+')
            pat = re.compile(regex)
            res = pat.split(self.raw)
            if len(res) > 2:
                self.version = res[2]
                return self
        return False
