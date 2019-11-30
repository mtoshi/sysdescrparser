# -*- coding: utf-8 -*-

"""sysdescrparser.cisco_iosxe."""


import re
from cisco import Cisco


# pylint: disable=no-member
class CiscoIOSXE(Cisco):

    """Class CiscoIOSXE.

    SNMP sysDescr for CiscoIOSXE.

    """

    def __init__(self, raw):
        """Constructor."""
        super(CiscoIOSXE, self).__init__(raw)
        self.os = 'IOSXE'
        self.model = self.UNKNOWN
        self.version = self.UNKNOWN

    def parse(self):
        """Parse."""
        main_version_name = "ios-xe"

        misc_version_names = ["gibraltar", "fuji", "everest", "denali", ]
        misc_version_names_regex = "|".join(
            rf"\[{version_name}\]"
            for version_name in misc_version_names
        )

        ios_xe_regex = f"{main_version_name}|{misc_version_names_regex}"

        ios_xe = re.search(
            ios_xe_regex, self.raw, flags=re.IGNORECASE
        )
        if not ios_xe:
            return False

        version_regex = r"version\s+(?P<version>[^\s,]+)"
        catched_version = re.search(
            version_regex, self.raw, flags=re.IGNORECASE
        )
        if catched_version:
            version = catched_version.groupdict()['version']
            self.version = version

        model_regex = r"software\s+\((?P<model>.*)\),"
        catched_model = re.search(model_regex, self.raw, flags=re.IGNORECASE)
        if catched_model:
            model = catched_model.groupdict()['model']
            self.model = model

        return self
