# -*- coding: utf-8 -*-

"""Sysdescrparser."""

import sys

# pylint: disable=unused-import
if sys.version_info.major == 2:
    from sysdescrparser import sysdescrparser
else:
    from sysdescrparser.sysdescrparser import sysdescrparser
