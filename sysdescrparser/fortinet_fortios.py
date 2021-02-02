import re
from fortinet import FortiNet


class FortiOs(FortiNet):
    """Class FortiOs.

    SNMP sysDescr for fortigate.

    """

    def __init__(self, raw):
        """Constructor."""
        super(FortiOs, self).__init__(raw)
        self.os = 'fortios'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        regex = r'Fortinet Firewall (.*) v((\d\.)*\d)'
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            self.model = res.group(1)
            self.version = res.group(2)
            return self

        return False
