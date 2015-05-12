# -*- coding: utf-8 -*-

"""sysdescrparser.hp_procurve."""


import re
from hp import HP


# pylint: disable=no-member
class HPProCurve(HP):

    """Class HPProCurve.

    SNMP sysDescr for HPProCurve.

    """

    def __init__(self, raw):
        """Constructor."""
        super(HPProCurve, self).__init__(raw)
        self.os = 'PROCURVE'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        pat = re.compile('ProCurve', re.I)
        res = pat.search(self.raw)
        if res:
            regex = r'^(.*), revision (.*), ROM'
            pat = re.compile(regex)
            res = pat.search(self.raw)
            if res:
                self.model = res.group(1)
                self.version = res.group(2)
                return self
        return False
