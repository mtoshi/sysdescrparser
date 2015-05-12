# -*- coding: utf-8 -*-

"""sysdescrparser.cisco_ios."""


import re
from cisco import Cisco


# pylint: disable=no-member
class CiscoIOS(Cisco):

    """Class CiscoIOS.

    SNMP sysDescr for CiscoIOS.

    """

    def __init__(self, raw):
        """Constructor."""
        super(CiscoIOS, self).__init__(raw)
        self.os = 'IOS'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = (r'Cisco Internetwork Operating System Software ..IOS'
                 r' .* Software \((.*)\), Version (.*), .*RELEASE')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        regex = (r'Cisco IOS Software,'
                 r'.* Software \((.*)\), Version (.*), .*RELEASE')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        return False
