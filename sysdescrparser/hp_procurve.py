# -*- coding: utf-8 -*-

"""sysdescrparser.hp_procurve."""


import re
from sysdescr import SysDescr


# pylint: disable=no-member
class HPProCurve(SysDescr):

    """Class HPProCurve.

    SNMP sysDescr for HP ProCurve.

    """

    def parse(self):
        """Parse."""
        vendor = 'HP'
        os = 'PROCURVE'
        model = self.UNKNOWN
        version = self.UNKNOWN

        pat = re.compile('ProCurve', re.I)
        res = pat.search(self.raw)
        if res:
            regex = r'^(.*), revision (.*), ROM'
            pat = re.compile(regex)
            res = pat.search(self.raw)
            if res:
                model = res.group(1)
                version = res.group(2)
                return self.store(vendor=vendor,
                                  os=os,
                                  model=model,
                                  version=version)
        return False
