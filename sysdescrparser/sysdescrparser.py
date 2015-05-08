# -*- coding: utf-8 -*-

"""sysdescrparser."""


import sys
import os
sys.path.append(os.path.dirname(__file__))

from cisco_ios import CiscoIOS
from cisco_nxos import CiscoNXOS
from cisco_iosxr import CiscoIOSXR
from juniper_junos import JuniperJunos
from juniper_screenos import JuniperScreenOS
from brocade_ironware import BrocadeIronWare
from brocade_serveriron import BrocadeServerIron
from brocade_networkos import BrocadeNetworkOS
from arista_eos import AristaEOS
from unknown import Unknown


def sysdescrparser(sysdescr):
    """Snmp sysDescr parsing."""
    #
    # cisco nxos
    #
    obj = CiscoNXOS(sysdescr)
    if obj.parse():
        return obj
    #
    # cisco iosxr
    #
    obj = CiscoIOSXR(sysdescr)
    if obj.parse():
        return obj
    #
    # cisco ios
    #
    obj = CiscoIOS(sysdescr)
    if obj.parse():
        return obj
    #
    # juniper junos
    #
    obj = JuniperJunos(sysdescr)
    if obj.parse():
        return obj
    #
    # juniper screenos
    #
    obj = JuniperScreenOS(sysdescr)
    if obj.parse():
        return obj
    #
    # brocade ironware
    #
    obj = BrocadeIronWare(sysdescr)
    if obj.parse():
        return obj
    #
    # brocade serveriron
    #
    obj = BrocadeServerIron(sysdescr)
    if obj.parse():
        return obj
    #
    # brocade networkos
    #
    obj = BrocadeNetworkOS(sysdescr)
    if obj.parse():
        return obj
    #
    # arista eos
    #
    obj = AristaEOS(sysdescr)
    if obj.parse():
        return obj
    #
    # Unknown
    #
    obj = Unknown(sysdescr)
    if obj.parse():
        return obj
