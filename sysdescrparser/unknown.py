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

    def parse(self):
        """Parse."""
        return super().parse()
