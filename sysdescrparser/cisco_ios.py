# -*- coding: utf-8 -*-

"""sysdescrparser.cisco_ios."""


import re
from sysdescr import SysDescr


# pylint: disable=no-member
class CiscoIOS(SysDescr):

    """Class CiscoIOS.

    SNMP sysDescr for Cisco IOS.

    """

    def parse(self):
        """Parse."""
        vendor = 'cisco'
        os = 'ios'
        series = self.UNKNOWN
        version = self.UNKNOWN

        regex = (r'Cisco Internetwork Operating System Software ..IOS'
                 r' .* Software \((.*)\), Version (.*), .*RELEASE')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            series = res.group(1)
            version = res.group(2)

        regex = (r'Cisco IOS Software,'
                 r'.* Software \((.*)\), Version (.*), .*RELEASE')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            series = res.group(1)
            version = res.group(2)

        return self._store(vendor, os, series, version)
