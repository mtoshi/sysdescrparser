# -*- coding: utf-8 -*-

"""sysdescrparser.unknown."""


from sysdescr import SysDescr


class Unknown(SysDescr):

    """Class Unknown.

    SNMP sysDescr for Unknown.

    """

    def parse(self):
        """Parse."""
        return self._store(self.UNKNOWN,
                           self.UNKNOWN,
                           self.UNKNOWN,
                           self.UNKNOWN)
