# -*- coding: utf-8 -*-

"""sysdescrparser.yamaha_rtx."""


import re
from yamaha import Yamaha


# pylint: disable=no-member
class YamahaRTX(Yamaha):

    """Class YamahaRTX.

    SNMP sysDescr for YamahaRTX.

    """

    def __init__(self, raw):
        """Constructor."""
        super(YamahaRTX, self).__init__(raw)
        self.os = 'RTX'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'^(RTX\w+)\s+(Rev..*)\s+\(.*\)$')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        return False
