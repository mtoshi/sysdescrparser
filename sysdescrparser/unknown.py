# -*- coding: utf-8 -*-

"""sysdescrparser.unknown."""


from sysdescr import SysDescr


class Unknown(SysDescr):

    """Class Unknown.

    SNMP sysDescr for Unknown.

    """

    def __init__(self, raw):
        """Constructor."""
        super(Unknown, self).__init__(raw)
        self.vendor = self.UNKNOWN
        self.model = self.UNKNOWN
        self.os = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        return self
