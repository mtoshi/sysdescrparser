# -*- coding: utf-8 -*-

"""UnitTests for sysdescrparser."""

import unittest
import os
import json
from sysdescrparser import sysdescrparser
from sysdescr import SysDescr


class UnitTests(unittest.TestCase):

    """Class UnitTest.

    Unit test for sysdescrparser.

    """

    def setUp(self):
        """Setup."""
        self.result_file = 'test_result.txt'
        self.here = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(self.here,
                            '..',
                            '..',
                            'samples',
                            'sample_data.json')
        self.descrs = json_load(path)

    def test_abstract(self):
        """test abstraction."""
        self.assertRaises(TypeError, SysDescr, 'xxxxxxxx')

        # pylint: disable=no-init,abstract-method
        class DoesNotHaveParse(SysDescr):

            """Abstract test class."""

            def aaaa(self):
                """Not parse method."""

        self.assertRaises(TypeError, DoesNotHaveParse)

    def test_parse(self):
        """test parsing."""
        path = os.path.join(self.here, self.result_file)
        remove(path)

        for descr in self.descrs:

            obj = sysdescrparser(descr['raw'])
            obj.parse()

            res = ' '.join([
                obj.vendor,
                obj.os,
                obj.model,
                obj.version,
                ' --- ',
                descr['vendor'],
                descr['os'],
                descr['model'],
                descr['version'],
                '\n',
            ])

            write(path, res)

            self.assertEqual(obj.vendor, descr['vendor'])
            self.assertEqual(obj.os, descr['os'])
            self.assertEqual(obj.model, descr['model'])
            self.assertEqual(obj.version, descr['version'])


def remove(path):
    """Remove file."""
    is_exists = os.path.isfile(path)
    if is_exists:
        os.remove(path)


def write(path, content):
    """Write to file."""
    with open(path, 'a') as _file:
        return _file.write(content)


def json_load(path):
    """Read test data."""
    with open(path) as _file:
        return json.load(_file)
