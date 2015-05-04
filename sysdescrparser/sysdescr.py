# -*- coding: utf-8 -*-

"""sysdescr."""


import sys

# pylint: disable=unused-import
if sys.version_info.major == 2:
    from sysdescr_py2 import SysDescr
else:
    from sysdescr_py3 import SysDescr
