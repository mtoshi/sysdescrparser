# -*- coding: utf-8 -*-

"""sysdescrparser.fundry_ironware."""


import re
from sysdescr import SysDescr


# pylint: disable=no-member
class FoundryIronWare(SysDescr):

    """Class FoundryIronWare.

    SNMP sysDescr for Foundry IronWare.

    """

    def parse(self):
        """Parse."""
        vendor = 'foundry'
        os = 'ironware'
        model = self.UNKNOWN
        version = self.UNKNOWN

        regex = (r'Foundry\s+Networks,\s+Inc.\s+'
                 r'(.*),\s+IronWare\s+Version\s+(.*)\s+Compiled')
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
