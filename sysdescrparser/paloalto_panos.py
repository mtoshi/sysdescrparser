# -*- coding: utf-8 -*-

"""sysdescrparser.paloalto_panos."""


import re
from paloalto import PaloAlto


# pylint: disable=no-member
class PaloAltoPANOS(PaloAlto):

    """Class PaloAltoPANOS.

    SNMP sysDescr for PaloAltoPANOS.

    """

    def __init__(self, raw):
        """Constructor."""
        super(PaloAltoPANOS, self).__init__(raw)
        self.os = 'PANOS'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'Palo\s+Alto\s+Networks\s+(.*)\s+series\s+')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            return self
        return False
