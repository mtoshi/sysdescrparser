# -*- coding: utf-8 -*-

"""sysdescrparser.freebsd."""

import re
from sysdescr import SysDescr


# pylint: disable=no-name-in-module
# pylint: disable=no-member
class FreeBSD(SysDescr):

    """Class FreeBSD.

    This class is only for vendor definition.

    """

    def __init__(self, raw):
        """Constructor."""
        super(FreeBSD, self).__init__(raw)
        self.vendor = self.UNKNOWN
        self.model = self.UNKNOWN
        self.os = 'FREEBSD'
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        regex = (r'^FreeBSD\s+')
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
