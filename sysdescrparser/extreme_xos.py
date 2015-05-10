# -*- coding: utf-8 -*-

"""sysdescrparser.extreme_xos."""


import re
from extreme import Extreme


# pylint: disable=no-member
class ExtremeXOS(Extreme):

    """Class ExtremeXOS.

    SNMP sysDescr for ExtremeXOS.

    """

    def __init__(self, raw):
        """Constructor."""
        super(ExtremeXOS, self).__init__(raw)
        self.os = 'XOS'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'ExtremeWare\s+X0S\s+version\s+(.*)\s+'
                 r'by\s+release-manager\s+on\s+')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.version = res.group(1)
            return self

        regex = (r'ExtremeXOS\s+version\s+(.*)\s+'
                 r'by\s+release-manager\s+on\s+')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.version = res.group(1)
            return self

        return False
