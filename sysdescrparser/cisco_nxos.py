# -*- coding: utf-8 -*-

"""sysdescrparser.cisco_nxos."""


import re
from cisco import Cisco


# pylint: disable=no-member
class CiscoNXOS(Cisco):

    """Class CiscoNXOS.

    SNMP sysDescr for CiscoNXOS.

    """

    def __init__(self, raw):
        """Constructor."""
        super(CiscoNXOS, self).__init__(raw)
        self.os = 'NXOS'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'Cisco\s+NX-OS.*,\s+'
                 r'Software\s+\((.*)\),\s+'
                 r'Version\s+(.*),'
                 r'\s+Interim\s+version\s+.* RELEASE SOFTWARE')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        regex = (r'Cisco\s+NX-OS.*,\s+'
                 r'Software\s+\((.*)\),'
                 r'\s+Version\s+(.*),\s+RELEASE\s+SOFTWARE')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        return False
