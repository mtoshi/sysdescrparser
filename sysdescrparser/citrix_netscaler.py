# -*- coding: utf-8 -*-

"""sysdescrparser.citrix_netscaler."""


import re
from sysdescr import SysDescr


# pylint: disable=no-member
class CitrixNetscaler(SysDescr):

    """Class CitrixNetscaler.

    SNMP sysDescr for Citrix Netscaler.

    """

    def parse(self):
        """Parse."""
        vendor = 'CITRIX'
        os = 'NETSCALER'
        model = self.UNKNOWN
        version = self.UNKNOWN

        regex = (r'^NetScaler\s+(.*:\s+Build\s+.*),\s+Date:\s+')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            version = res.group(1)
            return self.store(vendor=vendor,
                              os=os,
                              model=model,
                              version=version)
        return False
