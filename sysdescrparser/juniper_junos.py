# -*- coding: utf-8 -*-

"""sysdescrparser.juniper_junos."""


import re
from juniper import Juniper


# pylint: disable=no-member
class JuniperJunos(Juniper):

    """Class JuniperJunos.

    SNMP sysDescr for JuniperJUNOS.

    """

    def __init__(self, raw):
        """Constructor."""
        super(JuniperJunos, self).__init__(raw)
        self.os = 'JUNOS'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'Juniper\s+Networks,\s+Inc.'
                 r'\s+(.*)\s+(?:internet\s+router|Ethernet\sSwitch),'
                 r'\s+kernel\s+JUNOS\s+([A-Z0-9-.]*)(?:\s#|,\s)')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        regex = (r'Juniper\s+Networks,\s+Inc.'
                 r'\s+(.*)\s+Edge\s+.*\s+Version\s+:\s+\((.*)\)\s+Build')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        return False
