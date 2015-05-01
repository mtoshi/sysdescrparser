# -*- coding: utf-8 -*-

"""sysdescrparser."""


import re


class SysDescrParser(object):

    """Class SysDescrParser.

    SNMP sysDescr parser.

    """

    UNKNOWN = 'UNKNOWN'

    def __init__(self, raw):
        """Constructor."""
        self.raw = raw
        self.vendor = None
        self.os = None
        self.series = None
        self.version = None
        self.parse()

    def __str__(self):
        """string."""
        return self.vendor

    def _store(self, vendor, os, series, version):
        """Store attributes."""
        self.vendor = vendor
        self.os = os
        self.series = series
        self.version = version
        return self

    def parse_cisco_ios_series_version(self):
        """Parse cisco ios version."""
        regex = (r'Software \((.*)\), Version (.*), .*RELEASE SOFTWARE')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            return (res.group(1), res.group(2))
        return (self.UNKNOWN, self.UNKNOWN)

    def parse_cisco_ios(self):
        """Parse cisco ios."""
        vendor = 'cisco'
        os = 'cisco-ios'
        series, version = self.parse_cisco_ios_series_version()
        return self._store(vendor, os, series, version)

    def parse(self):
        """Parse."""
        pat = re.compile(r'^Cisco .* Software ..IOS|^Cisco IOS')
        if pat.search(self.raw):
            self.parse_cisco_ios()

        else:
            print('[error] not support "%s".' % self.raw)
            self._store(self.UNKNOWN,
                        self.UNKNOWN,
                        self.UNKNOWN,
                        self.UNKNOWN)
        return self
