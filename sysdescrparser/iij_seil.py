# -*- coding: utf-8 -*-

"""sysdescrparser.iij_seil."""


import re
from iij import IIJ


# pylint: disable=no-member
class IIJSeil(IIJ):

    """Class IIJSeil.

    SNMP sysDescr for IIJSeil.

    """

    def __init__(self, raw):
        """Constructor."""
        super(IIJSeil, self).__init__(raw)
        self.os = 'SEIL'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = r'(SEIL\/.*)\s+ver\s+(.*)\s+\(.*\)'
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self
        return False
