# -*- coding: utf-8 -*-

"""sysdescrparser.juniper_junos."""


import re
from sysdescr import SysDescr


# pylint: disable=no-member
class JuniperJunos(SysDescr):

    """Class JuniperJunos.

    SNMP sysDescr for Juniper JUNOS.

    """

    def parse(self):
        """Parse."""
        vendor = 'juniper'
        os = 'junos'
        series = self.UNKNOWN
        version = self.UNKNOWN

        regex = (r'Juniper\s+Networks,\s+Inc.'
                 r'\s+(.*)\s+internet\s+router,\s+kernel\s+JUNOS\s+(.*) #')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            series = res.group(1)
            version = res.group(2)
            return self._store(vendor=vendor,
                               os=os,
                               series=series,
                               version=version)

        regex = (r'Juniper\s+Networks,\s+Inc.'
                 r'\s+(.*)\s+Edge\s+.*\s+Version\s+:\s+\((.*)\)\s+Build')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            series = res.group(1)
            version = res.group(2)
            return self._store(vendor=vendor,
                               os=os,
                               series=series,
                               version=version)
        return False
