# -*- coding: utf-8 -*-

"""sysdescrparser.sun_sunos."""


import re
from sun import Sun


# pylint: disable=no-member
class SunSUNOS(Sun):

    """Class SunSUNOS.

    SNMP sysDescr for SunSUNOS.

    """

    def __init__(self, raw):
        """Constructor."""
        super(SunSUNOS, self).__init__(raw)
        self.os = 'SUNOS'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'SunOS\s+(\d+.\d+)\s+.*,(.*),\s+')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.version = res.group(1)
            self.model = res.group(2)
            return self

        regex = (r'SunOS\s+(\d+.\d+)\s+.*,(.*)$')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.version = res.group(1)
            self.model = res.group(2)
            return self

        return False
