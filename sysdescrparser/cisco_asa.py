# -*- coding: utf-8 -*-

"""sysdescrparser.cisco_iosxe."""

import re
from cisco import Cisco


# pylint: disable=no-member
class CiscoASA(Cisco):
    """Class CiscoASA.

    SNMP sysDescr for CiscoASA.

    """

    def __init__(self, raw):
        """Constructor."""
        super(CiscoASA, self).__init__(raw)
        self.os = 'Adaptive_Security_Appliance'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'Cisco Adaptive Security Appliance '
                 r'Version (\d.*)')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.version = res.group(1)
            return self

        return False



