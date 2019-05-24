===================================================
sysdescrparser
===================================================

Sysdescparser is a utility tool for network operators.
This module parses SNMP sysDescr(OID: 1.3.6.1.2.1.1.1).

Recent IP equipments are implemented useful API.
However connection method is different with each vendor.
In case of multi-vendor environment,
we have to check each target node's information such as vendor name and os name.
I think checking of SNMP sysDescr is a very efficient as a unified method for pre-filter.
This module parses sysDescr value with vendor name, model name, os name and os version as far as possible.
However, the sysDescr is free format.
It does not guarantee that these information always exists. Unknown value, assigns the UNKNOWN.
If you have any need to handle the equipment that this module does not support,
then please send the sysDescr value to this package author.
Or, please contact using function of the such as github pull request.

.. image:: https://secure.travis-ci.org/mtoshi/sysdescrparser.svg?branch=master
   :target: http://travis-ci.org/mtoshi/sysdescrparser
.. image:: https://coveralls.io/repos/mtoshi/sysdescrparser/badge.svg?branch=master
   :target: https://coveralls.io/r/mtoshi/sysdescrparser?branch=master
.. image:: https://img.shields.io/pypi/v/sysdescrparser.svg
   :target: https://pypi.python.org/pypi/sysdescrparser/
   :alt: Latest Version

Requirements
-------------
* Python2.7, 3.5, 3.6, 3.7, PyPy.

Instration
-----------
* PyPI or Github. ::

    $ pip install sysdescrpaser
    
    or
    
    $ git clone https://github.com/mtoshi/sysdescrparser
    $ cd sysdescrparser
    $ sudo python setup.py install


Using example
--------------
* Example for Juniper Junos sysDescr ::

    >>> from sysdescrparser import sysdescrparser
    >>> sysdescr = sysdescrparser('Juniper Networks, Inc. ex2200-48t-4g internet router, kernel JUNOS 10.2R1.8 #0: 2010-05-27 20:13:49 UTC')
    >>> sysdescr.vendor
    'JUNIPER'
    >>> sysdescr.model
    'ex2200-48t-4g'
    >>> sysdescr.os
    'JUNOS'
    >>> sysdescr.version
    '10.2R1.8'


* Example for Cisco CiscoIOS sysDescr ::

    >>> sysdescr = sysdescrparser('Cisco IOS Software, c7600s72033_rp Software (c7600s72033_rp-ADVIPSERVICESK9-M), Version 12.2(33)SRC5, RELEASE SOFTWARE (fc2)')
    >>> sysdescr.vendor
    'CISCO'
    >>> sysdescr.model
    'c7600s72033_rp-ADVIPSERVICESK9-M'
    >>> sysdescr.os
    'IOS'
    >>> sysdescr.version
    '12.2(33)SRC5'


* Example for Brocade VDX sysDescr ::

    >>> sysdescr = sysdescrparser('Brocade VDX Switch.')
    >>> sysdescr.vendor
    'BROCADE'
    >>> sysdescr.model
    'VDX'
    >>> sysdescr.os
    'NOS'
    >>> sysdescr.version
    'UNKNOWN'


Parsing logic and Support Vendor and OS
----------------------------------------
* About parsing logic and support of vendor and os.
    Of course you are able to see this python code and also see how it works easily from sample data.
    https://github.com/mtoshi/sysdescrparser/blob/master/samples/sample_data.json
    It will be able to understand almost.
    (Sometimes, using hard code. And also using UNKNOWN values.)
    This sample data is also used directly by code test.

* About uncovered vendor and os.
    If you have any need to handle the equipment that this module does not support,
    then please send the sysDescr value to this package author.
    Or, please contact using function of the such as github pull request.

* If you already enabled SNMP daemon, then you can get sysDescr value with below. ::

    % snmpwalk -Os -v 2c -c your_community_string localhost 1.3.6.1.2.1.1.1
    sysDescr.0 = STRING: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

    % snmpget -Os -v 2c -c your_community_string localhost 1.3.6.1.2.1.1.1.0
    sysDescr.0 = STRING: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

