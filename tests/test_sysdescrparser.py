# -*- coding: utf-8 -*-

"""UnitTests for sysdescrparser."""

import unittest
from sysdescrparser import SysDescrParser


class UnitTests(unittest.TestCase):

    """Class UnitTest.

    Unit test for SysDescrParser.

    """

    def setUp(self):
        """Setup."""
        self.raw = ' '.join(['Cisco IOS Software,',
                             'C1234 Software (C1234-ABCD),',
                             'Version 1.1(11)ABC1, RELEASE SOFTWARE (ABC1)',
                             'Copyright (c) 1998-2008 by Cisco Systems, Inc.',
                             'Compiled Mon 01-Jan-01 00:00 by aaaaa'])
        self.obj = SysDescrParser(self.raw)

    def test_str(self):
        """test str."""
        self.assertEqual(self.obj.vendor, "cisco")

    def test_parse(self):
        """test parse."""
        self.assertEqual(self.obj.raw, self.raw)
        self.assertEqual(self.obj.vendor, 'cisco')
        self.assertEqual(self.obj.os, 'cisco-ios')
        self.assertEqual(self.obj.series, 'C1234-ABCD')
        self.assertEqual(self.obj.version, '1.1(11)ABC1')
