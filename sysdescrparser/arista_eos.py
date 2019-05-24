# -*- coding: utf-8 -*-

"""sysdescrparser.arista_eos."""


import re
from arista import Arista


# pylint: disable=no-member
class AristaEOS(Arista):

    """Class AristaEOS.

    SNMP sysDescr for AristaEOS.

    """

    def __init__(self, raw):
        """Constructor."""
        super(AristaEOS, self).__init__(raw)
        self.os = 'EOS'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'Arista\s+Networks\s+EOS\s+'
                 r'version\s+(.*)\s+'
                 r'running\s+on\s+(?:an\s+Arista\s+Networks|a)\s+(.*)$')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.version = res.group(1)
            self.model = res.group(2)
            return self
        return False
