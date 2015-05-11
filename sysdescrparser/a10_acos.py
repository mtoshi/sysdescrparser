# -*- coding: utf-8 -*-

"""sysdescrparser.a10_acos."""


import re
from a10 import A10


# pylint: disable=no-member
class A10ACOS(A10):

    """Class A10ACOS.

    SNMP sysDescr for A10ACOS.

    """

    def __init__(self, raw):
        """Constructor."""
        super(A10ACOS, self).__init__(raw)
        self.os = 'ACOS'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'^AX\s+Series\s+Advanced\s+Traffic\s+Manager\s+(.*),\s+'
                 r'.*\s+version\s+(.*),')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self
        return False
