# -*- coding: utf-8 -*-

"""sysdescrparser.brocade_ironware."""


import re
from brocade import Brocade


# pylint: disable=no-member
class BrocadeIronWare(Brocade):

    """Class BrocadeIronWare.

    SNMP sysDescr for Brocade IronWare.

    """

    def __init__(self, raw):
        """Constructor."""
        super(BrocadeIronWare, self).__init__(raw)
        self.os = 'IRONWARE'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'Brocade Communications Systems, Inc. (.*), '
                 r'IronWare Version (.*) Compiled')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        regex = (r'Brocade .* \(System Mode: (.*)\), '
                 r'IronWare Version (.*) Compiled')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        regex = (r'Brocade NetIron (.*), '
                 r'IronWare Version (.*) Compiled')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        return False
