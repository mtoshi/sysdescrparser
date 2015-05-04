# -*- coding: utf-8 -*-

"""sysdescrparser.cisco_ios."""


import re
from sysdescr import SysDescr


# pylint: disable=no-member
class JuniperJunos(SysDescr):

    """Class JuniperJunos.

    SNMP sysDescr for Juniper JUNOS.

    """

    def __init__(self, raw):
        """Constructor."""
        super(JuniperJunos, self).__init__(raw)

    def parse(self):
        """Parse."""
        vendor = 'juniper'
        os = 'junos'
        series = self.UNKNOWN
        version = self.UNKNOWN

        regex = (r'Inc. (.*) internet router, kernel JUNOS (.*) #')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            series = res.group(1)
            version = res.group(2)

        regex = (r'Inc. (.*) Edge .* Version : \((.*)\) Build')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            series = res.group(1)
            version = res.group(2)

        return self._store(vendor, os, series, version)
