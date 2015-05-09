# -*- coding: utf-8 -*-

"""sysdescrparser.juniper_screenos."""


import re
from sysdescr import SysDescr


# pylint: disable=no-member
class JuniperScreenOS(SysDescr):

    """Class JuniperScreenOS.

    SNMP sysDescr for Juniper ScreenOS.

    """

    def parse(self):
        """Parse."""
        vendor = 'JUNIPER'
        os = 'SCREENOS'
        model = self.UNKNOWN
        version = self.UNKNOWN

        regex = (r'^(SSG.*)\s+version\s+(.*)\s+\(SN:.*\)')
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
