# -*- coding: utf-8 -*-

"""sysdescrparser.sysdescr."""


from abc import ABCMeta
from abc import abstractmethod
# pylint: disable=no-name-in-module


def metaclass(mcls):
    """Meta class."""
    def decorator(cls):
        """Decorator."""
        body = vars(cls).copy()
        body.pop('__dict__', None)
        body.pop('__weakref__', None)
        return mcls(cls.__name__, cls.__bases__, body)
    return decorator


# pylint: disable=R0205
@metaclass(ABCMeta)
class SysDescr(object):

    """Class SysDescr.

    SNMP sysDescr.

    This class is abstract.

    Attributes:

        :raw (str): SNMP sysDescr raw string.
        :vendor (str): = Vendor name. Default is None.
        :model (str): = Model name. Default is None.
        :os (str): = OS name. Default is None.
        :version (str): = Version information. Default is None.

    Abstract methods:

        :parse: Sub class has to implement this parse method.

    """

    UNKNOWN = 'UNKNOWN'

    def __init__(self, raw):
        """Constructor.

        Args:

            :raw (str): SNMP sysDescr raw string.

        """
        self.raw = raw
        self.vendor = None
        self.model = None
        self.os = None
        self.version = None

    @abstractmethod
    def parse(self):
        """Parsing for sysDescr value.

        Sub class has to implement this method.

        """
