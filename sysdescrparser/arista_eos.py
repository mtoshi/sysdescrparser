# -*- coding: utf-8 -*-

"""sysdescrparser.arista_eos."""


import re
from sysdescr import SysDescr


# pylint: disable=no-member
class AristaEOS(SysDescr):

    """Class AristaEOS.

    SNMP sysDescr for Arista EOS.

    """

    def parse(self):
        """Parse."""
        vendor = 'arista'
        os = 'eos'
        model = self.UNKNOWN
        version = self.UNKNOWN

        regex = (r'Arista\s+Networks\s+EOS\s+'
                 r'version\s+(.*)\s+'
                 r'running\s+on\s+an\s+Arista\s+Networks\s+(.*)$')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            version = res.group(1)
            model = res.group(2)
            return self._store(vendor=vendor,
                               os=os,
                               model=model,
                               version=version)
        return False
