# -*- coding: utf-8 -*-

"""sysdescrparser.citrix_netscaler."""


import re
from citrix import Citrix


# pylint: disable=no-member
class CitrixNetscaler(Citrix):

    """Class CitrixNetscaler.

    SNMP sysDescr for CitrixNetscaler.

    """

    def __init__(self, raw):
        """Constructor."""
        super(CitrixNetscaler, self).__init__(raw)
        self.os = 'NETSCALER'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'^NetScaler\s+(.*:\s+Build\s+.*),\s+Date:\s+')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.version = res.group(1)
            return self
        return False
