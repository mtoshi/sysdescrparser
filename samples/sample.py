# -*- coding: utf-8 -*-

"""Sample code."""

import os
import json
from sysdescrparser import sysdescrparser


def main():
    """Sample main."""
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, 'sample_data.json')

    with open(path) as _file:
        descrs = json.load(_file)

    for descr in descrs:
        sysdescr = sysdescrparser(descr['raw'])
        print('#'*80)
        print('Vendor: %s' % sysdescr.vendor)
        print('Model: %s' % sysdescr.model)
        print('OS: %s' % sysdescr.os)
        print('Version: %s' % sysdescr.version)


if __name__ == "__main__":

    main()
