# -*- coding: utf-8 -*-

"""sysdescrparser.fundry_ironware."""


import re
from foundry import Foundry


# pylint: disable=no-member
class FoundryIronWare(Foundry):

    """Class FoundryIronWare.

    SNMP sysDescr for FoundryIronWare.

    """

    def __init__(self, raw):
        """Constructor."""
        super(FoundryIronWare, self).__init__(raw)
        self.os = 'IRONWARE'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'Foundry\s+Networks,\s+Inc.\s+'
                 r'(.*),\s+IronWare\s+Version\s+(.*)\s+Compiled')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self
        return False
