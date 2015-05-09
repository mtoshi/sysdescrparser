# -*- coding: utf-8 -*-

"""sysdescrparser.cisco_iosxr."""


import re
from sysdescr import SysDescr


# pylint: disable=no-member
class CiscoIOSXR(SysDescr):

    """Class CiscoIOSXR.

    SNMP sysDescr for Cisco IOSXR.

    """

    def parse(self):
        """Parse."""
        vendor = 'CISCO'
        os = 'IOSXR'
        model = self.UNKNOWN
        version = self.UNKNOWN

        regex = (r'Cisco\s+IOS\s+XR\s+'
                 r'Software\s+\((.*)\),\s+Version\s+(.*\[.*\])')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            model = res.group(1)
            version = res.group(2)
            return self.store(vendor=vendor,
                              os=os,
                              model=model,
                              version=version)
        return False
