# -*- coding: utf-8 -*-

"""sysdescrparser.cisco_ios."""


import re
from sysdescr import SysDescr


# pylint: disable=no-member
class CiscoIOSXR(SysDescr):

    """Class CiscoIOSXR.

    SNMP sysDescr for Cisco IOSXR.

    """

    def __init__(self, raw):
        """Constructor."""
        super(CiscoIOSXR, self).__init__(raw)

    def parse(self):
        """Parse."""
        vendor = 'cisco'
        os = 'iosxr'
        series = self.UNKNOWN
        version = self.UNKNOWN

        regex = (r'Software \(Cisco (.*) Series\), Version (.*\[.*\])')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            series = res.group(1)
            version = res.group(2)
            return self._store(vendor, os, series, version)

        regex = (r'Software \(Cisco (.*)\), Version (.*\[.*\])')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            series = res.group(1)
            version = res.group(2)
            return self._store(vendor, os, series, version)

        return (self.UNKNOWN, self.UNKNOWN)
