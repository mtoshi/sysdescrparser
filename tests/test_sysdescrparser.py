# -*- coding: utf-8 -*-

"""UnitTests for sysdescrparser."""

import unittest
import os
import json
from sysdescrparser import SysDescrParser


class UnitTests(unittest.TestCase):

    """Class UnitTest.

    Unit test for SysDescrParser.

    """

    def setUp(self):
        """Setup."""
        here = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(here, 'test_data.json')
        self.descrs = json_load(path)

    def test_parse(self):
        """test parse."""
        for descr in self.descrs:
            obj = SysDescrParser(descr['raw'])
            self.assertEqual(obj.vendor, descr['vendor'])
            self.assertEqual(obj.os, descr['os'])
            self.assertEqual(obj.series, descr['series'])
            self.assertEqual(obj.version, descr['version'])


def json_load(path):
    """Read test data."""
    with open(path) as _file:
        return json.load(_file)
