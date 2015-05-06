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
        series = self.UNKNOWN
        version = self.UNKNOWN

        regex = (r'version (.*) running on an Arista Networks (.*)$')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            version = res.group(1)
            series = res.group(2)

        return self._store(vendor, os, series, version)
