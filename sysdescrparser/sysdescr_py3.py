# -*- coding: utf-8 -*-

"""sysdescrparser."""


from abc import ABCMeta
from abc import abstractmethod


# pylint: disable=no-name-in-module
class SysDescr(object, metaclass=ABCMeta):

    """Class SysDescr.

    SNMP sysDescr.

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

    def _store(self, vendor, os, series, version):
        """Store attributes."""
        self.vendor = vendor
        self.os = os
        self.series = series
        self.version = version
        return self

    @abstractmethod
    def parse(self):
        """Parsing."""
        self._store(self.UNKNOWN,
                    self.UNKNOWN,
                    self.UNKNOWN,
                    self.UNKNOWN)
        return self
