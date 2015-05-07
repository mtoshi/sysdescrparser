# -*- coding: utf-8 -*-

"""sysdescrparser.unknown."""


from sysdescr import SysDescr


class Unknown(SysDescr):

    """Class Unknown.

    SNMP sysDescr for Unknown.

    """

    def parse(self):
        """Parse."""
        return self._store(vendor=self.UNKNOWN,
                           os=self.UNKNOWN,
                           series=self.UNKNOWN,
                           version=self.UNKNOWN)
