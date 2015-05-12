# -*- coding: utf-8 -*-

"""sysdescrparser.cisco_iosxr."""


import re
from cisco import Cisco


# pylint: disable=no-member
class CiscoIOSXR(Cisco):

    """Class CiscoIOSXR.

    SNMP sysDescr for CiscoIOSXR.

    """

    def __init__(self, raw):
        """Constructor."""
        super(CiscoIOSXR, self).__init__(raw)
        self.os = 'IOSXR'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'Cisco\s+IOS\s+XR\s+'
                 r'Software\s+\((.*)\),\s+Version\s+(.*\[.*\])')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        return False
