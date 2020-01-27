# -*- coding: utf-8 -*-

"""sysdescrparser.mikrotik_routeros."""

from sysdescr import SysDescr
import re


# pylint: disable=no-member
class MikroTikRouterOS(SysDescr):

    """Class MikroTikRouterOS.

    SNMP sysDescr for MikroTikRouterOs.

    """

    def __init__(self, raw):
        """Constructor."""
        super(MikroTikRouterOS, self).__init__(raw)
        self.vendor = 'MikroTik'
        self.os = 'RouterOS'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = r"RouterOS\s+([\d.]+)\s+\(([\w|-]+)\)\s+on\s+([\w\-\+]+)"
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.version = res.group(1)
            self.model = res.group(3)
            return self

        return False
