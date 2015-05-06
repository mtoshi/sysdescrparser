# -*- coding: utf-8 -*-

"""sysdescrparser."""


import re
import sys
import os
sys.path.append(os.path.dirname(__file__))

from cisco_ios import CiscoIOS
from cisco_nxos import CiscoNXOS
from cisco_iosxr import CiscoIOSXR
from juniper_junos import JuniperJunos
from brocade_ironware import BrocadeIronWare
from brocade_serveriron import BrocadeServerIron
from brocade_networkos import BrocadeNetworkOS
from arista_eos import AristaEOS
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
    #
    # brocade ironware
    #
    elif re.compile(r'^Brocade .* IronWare ').search(sysdescr):
        return BrocadeIronWare(sysdescr)
    #
    # brocade serveriron
    #
    elif re.compile(r'^Brocade .* ServerIron ').search(sysdescr):
        return BrocadeServerIron(sysdescr)
    #
    # brocade networkos
    #
    elif re.compile(r'^Brocade VDX Switch.$').search(sysdescr):
        return BrocadeNetworkOS(sysdescr)
    #
    # arista eos
    #
    elif re.compile(r'^Arista Networks EOS').search(sysdescr):
        return AristaEOS(sysdescr)
    #
    # Unknown
    #
    else:
        return Unknown(sysdescr)
