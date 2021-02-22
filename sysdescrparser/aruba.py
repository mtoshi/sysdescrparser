# -*- coding: utf-8 -*-

"""sysdescrparser.aruba."""

import re
from sysdescr import SysDescr


# pylint: disable=no-name-in-module
# pylint: disable=no-member
class Aruba(SysDescr):

    """Class Aruba.

    This class is only for vendor definition.

    """

    def __init__(self, raw):
        """Constructor."""
        super(Aruba, self).__init__(raw)
        self.vendor = 'ARUBA'
        self.model = self.UNKNOWN
        self.os = 'ArubaOS'
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        regex = (r'ArubaOS'
                 r'.* \(MODEL: (?:Aruba)?(.*)\), Version (.*)')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        return False
