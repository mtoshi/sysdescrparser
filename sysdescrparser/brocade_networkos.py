# -*- coding: utf-8 -*-

"""sysdescrparser.brocade_serveriron."""


import re
from brocade import Brocade


# pylint: disable=no-member
class BrocadeNetworkOS(Brocade):

    """Class BrocadeNetworkOS.

    SNMP sysDescr for BrocadeNetworkOS.

    """

    def __init__(self, raw):
        """Constructor."""
        super(BrocadeNetworkOS, self).__init__(raw)
        self.os = 'NOS'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'^Brocade (.*) Switch.$')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            return self
        return False
