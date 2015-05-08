# -*- coding: utf-8 -*-

"""sysdescrparser.brocade_serveriron."""


import re
from sysdescr import SysDescr


# pylint: disable=no-member
class BrocadeServerIron(SysDescr):

    """Class BrocadeServerIron.

    SNMP sysDescr for Brocade ServerIron.

    """

    def parse(self):
        """Parse."""
        vendor = 'brocade'
        os = 'serveriron'
        model = self.UNKNOWN
        version = self.UNKNOWN

        regex = (r'Systems, Inc. ServerIron (.*), .* Version (.*)$')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            model = res.group(1)
            version = res.group(2)
            return self._store(vendor=vendor,
                               os=os,
                               model=model,
                               version=version)
        return False
