# -*- coding: utf-8 -*-

"""sysdescrparser.brocade_ironware."""


import re
from sysdescr import SysDescr


# pylint: disable=no-member
class BrocadeIronWare(SysDescr):

    """Class BrocadeIronWare.

    SNMP sysDescr for Brocade IronWare.

    """

    def parse(self):
        """Parse."""
        vendor = 'brocade'
        os = 'ironware'
        series = self.UNKNOWN
        version = self.UNKNOWN

        regex = (r'Brocade Communications Systems, Inc. (.*), '
                 r'IronWare Version (.*) Compiled')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            series = res.group(1)
            version = res.group(2)
            return self._store(vendor, os, series, version)

        regex = (r'Brocade .* \(System Mode: (.*)\), '
                 r'IronWare Version (.*) Compiled')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            series = res.group(1)
            version = res.group(2)
            return self._store(vendor, os, series, version)

        regex = (r'Brocade NetIron (.*), '
                 r'IronWare Version (.*) Compiled')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            series = res.group(1)
            version = res.group(2)
            return self._store(vendor, os, series, version)

        return False
