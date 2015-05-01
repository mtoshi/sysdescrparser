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
        regex = (r'Software \((.*)\), Version (.*), .*RELEASE')
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

    def parse_cisco_nxos_series_version(self):
        """Parse cisco nxos version."""
        regex = (r'Software \((.*)\), Version (.*), Interim version .*RELEASE')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            return (res.group(1), res.group(2))

        regex = (r'Software \((.*)\), Version (.*), .*RELEASE')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            return (res.group(1), res.group(2))

        return (self.UNKNOWN, self.UNKNOWN)

    def parse_cisco_nxos(self):
        """Parse cisco nxos."""
        vendor = 'cisco'
        os = 'cisco-nxos'
        series, version = self.parse_cisco_nxos_series_version()
        return self._store(vendor, os, series, version)

    def parse_cisco_iosxr_series_version(self):
        """Parse cisco iosxr version."""
        regex = (r'Software \(Cisco (.*) Series\), Version (.*\[.*\])')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            return (res.group(1), res.group(2))

        regex = (r'Software \(Cisco (.*)\), Version (.*\[.*\])')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            return (res.group(1), res.group(2))

        return (self.UNKNOWN, self.UNKNOWN)

    def parse_cisco_iosxr(self):
        """Parse cisco iosxr."""
        vendor = 'cisco'
        os = 'cisco-iosxr'
        series, version = self.parse_cisco_iosxr_series_version()
        return self._store(vendor, os, series, version)

    def parse_arista_eos_series_version(self):
        """Parse arista eos series version."""
        regex = (r'version (.*) running on an')
        pat = re.compile(regex)
        print(self.raw)
        res = pat.search(self.raw)
        if res:
            return (self.UNKNOWN, res.group(1))

        return (self.UNKNOWN, self.UNKNOWN)

    def parse_arista_eos(self):
        """Parse arista eos."""
        vendor = 'arista'
        os = 'eos'
        series, version = self.parse_arista_eos_series_version()
        return self._store(vendor, os, series, version)

    def parse(self):
        """Parse."""
        # cisco ios
        if re.compile(
                r'^Cisco .* Software ..IOS|^Cisco IOS Soft').search(self.raw):
            self.parse_cisco_ios()

        # cisco nxos
        elif re.compile(r'^Cisco NX-OS').search(self.raw):
            self.parse_cisco_nxos()

        # cisco iosxr
        elif re.compile(r'^Cisco IOS XR').search(self.raw):
            self.parse_cisco_iosxr()

        # arista eos
        elif re.compile(r'^Arista Networks EOS').search(self.raw):
            self.parse_arista_eos()

        else:
            print('[error] not support "%s".' % self.raw)
            self._store(self.UNKNOWN,
                        self.UNKNOWN,
                        self.UNKNOWN,
                        self.UNKNOWN)
        return self
