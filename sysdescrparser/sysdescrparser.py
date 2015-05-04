# -*- coding: utf-8 -*-

"""sysdescrparser."""


import sys
import os
import re
sys.path.append(os.path.dirname(__file__))
from cisco_ios import CiscoIOS
from cisco_nxos import CiscoNXOS
from cisco_iosxr import CiscoIOSXR
from juniper_junos import JuniperJunos
from unknown import Unknown


def sysdescrparser(sysdescr):
    """Snmp sysDescr parsing."""
    #
    # cisco ios
    #
    if re.compile(r'^Cisco .* Software ..IOS').search(sysdescr):
        return CiscoIOS(sysdescr)

    elif re.compile(r'^Cisco IOS Soft').search(sysdescr):
        return CiscoIOS(sysdescr)
    #
    # cisco nxos
    #
    elif re.compile(r'^Cisco NX-OS').search(sysdescr):
        return CiscoNXOS(sysdescr)

    #
    # cisco iosxr
    #
    elif re.compile(r'^Cisco IOS XR').search(sysdescr):
        return CiscoIOSXR(sysdescr)
    #
    # juniper junos
    #
    elif re.compile(r'^Juniper Networks').search(sysdescr):
        return JuniperJunos(sysdescr)

    # # arista eos
    # elif re.compile(r'^Arista Networks EOS').search(sysdescr):
    #     self.parse_arista_eos()

    #
    # Unknown
    #
    else:
        return Unknown(sysdescr)
