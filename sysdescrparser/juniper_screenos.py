# -*- coding: utf-8 -*-

"""sysdescrparser.juniper_screenos."""


import re
from juniper import Juniper


# pylint: disable=no-member
class JuniperScreenOS(Juniper):

    """Class JuniperScreenOS.

    SNMP sysDescr for JuniperScreenOS.

    """

    def __init__(self, raw):
        """Constructor."""
        super(JuniperScreenOS, self).__init__(raw)
        self.os = 'SCREENOS'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'^(SSG.*|NetScreen.*)\s+version\s+(.*)\s+\(SN:.*\)')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self
        return False
