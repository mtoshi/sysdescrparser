# -*- coding: utf-8 -*-

"""sysdescrparser.brocade_serveriron."""


import re
from brocade import Brocade


# pylint: disable=no-member
class BrocadeServerIron(Brocade):

    """Class BrocadeServerIron.

    SNMP sysDescr for Brocade ServerIron.

    """

    def __init__(self, raw):
        """Constructor."""
        super(BrocadeServerIron, self).__init__(raw)
        self.os = 'SERVERIRON'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'Systems, Inc. ServerIron (.*), .* Version (.*)$')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        return False
