# -*- coding: utf-8 -*-

"""sysdescrparser.cisco_ios."""


import re
from sysdescr import SysDescr


# pylint: disable=no-member
class CiscoNXOS(SysDescr):

    """Class CiscoNXOS.

    SNMP sysDescr for Cisco NXOS.

    """

    def parse(self):
        """Parse."""
        vendor = 'cisco'
        os = 'nxos'
        series = self.UNKNOWN
        version = self.UNKNOWN

        regex = (r'Cisco\s+NX-OS.*,\s+'
                 r'Software\s+\((.*)\),\s+'
                 r'Version\s+(.*),'
                 r'\s+Interim\s+version\s+.* RELEASE SOFTWARE')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            series = res.group(1)
            version = res.group(2)
            return self._store(vendor, os, series, version)

        regex = (r'Cisco\s+NX-OS.*,\s+'
                 r'Software\s+\((.*)\),'
                 r'\s+Version\s+(.*),\s+RELEASE\s+SOFTWARE')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            series = res.group(1)
            version = res.group(2)
            return self._store(vendor, os, series, version)

        return False
