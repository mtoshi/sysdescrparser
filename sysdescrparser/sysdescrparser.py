# -*- coding: utf-8 -*-

"""sysdescrparser."""


import sys
import os
sys.path.append(os.path.dirname(__file__))

# pylint: disable=C0413
from cisco_ios import CiscoIOS
from cisco_nxos import CiscoNXOS
from cisco_iosxr import CiscoIOSXR
from juniper_junos import JuniperJunos
from juniper_screenos import JuniperScreenOS
from brocade_ironware import BrocadeIronWare
from brocade_serveriron import BrocadeServerIron
from brocade_networkos import BrocadeNetworkOS
from foundry_ironware import FoundryIronWare
from arista_eos import AristaEOS
from hp_procurve import HPProCurve
from extreme_xos import ExtremeXOS
from paloalto_panos import PaloAltoPANOS
from a10_acos import A10ACOS
from citrix_netscaler import CitrixNetscaler
from linux import Linux
from sun_sunos import SunSUNOS
from freebsd import FreeBSD
from iij_seil import IIJSeil
from yamaha_rtx import YamahaRTX
from unknown import Unknown


def sysdescrparser(sysdescr):
    """SNMP sysDescr parsing.

    Args:

        :sysdescr(str): SNMP sysDescr raw string.

    Returns:

        :SysDescr sub-class instance: SysDescr is abstract super class.
            Each vendor class extends Sysdescr class and following attributes.

            :vendor(str): Vendor name.
            :model(str): Product Model name.
            :os(str): OS name.
            :version(str): OS version name.

    Example:

        .. code-block:: python

            >>> from sysdescrparser import sysdescrparser
            >>> sysdescr = sysdescrparser('Juniper Networks, Inc. ...')
            >>> sysdescr.vendor
            'JUNIPER'
            >>> sysdescr.model
            'ex2200-48t-4g'
            >>> sysdescr.os
            'JUNOS'
            >>> sysdescr.version
            '10.2R1.8'

    Support:

         Currently supported Vendor and OS.

         https://github.com/mtoshi/sysdescrparser/blob/master/samples/sample_data.json

    See also:

         https://github.com/mtoshi/sysdescrparser/blob/master/README.rst

    """
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
    # foundry ironware
    #
    obj = FoundryIronWare(sysdescr)
    if obj.parse():
        return obj
    #
    # arista eos
    #
    obj = AristaEOS(sysdescr)
    if obj.parse():
        return obj
    #
    # extreme xos
    #
    obj = ExtremeXOS(sysdescr)
    if obj.parse():
        return obj
    #
    # hp procurve
    #
    obj = HPProCurve(sysdescr)
    if obj.parse():
        return obj
    #
    # paloalto panos
    #
    obj = PaloAltoPANOS(sysdescr)
    if obj.parse():
        return obj
    #
    # a10 acos
    #
    obj = A10ACOS(sysdescr)
    if obj.parse():
        return obj
    #
    # citrix netscaler
    #
    obj = CitrixNetscaler(sysdescr)
    if obj.parse():
        return obj
    #
    # linux
    #
    obj = Linux(sysdescr)
    if obj.parse():
        return obj
    #
    # sun sunos
    #
    obj = SunSUNOS(sysdescr)
    if obj.parse():
        return obj
    #
    # freebsd
    #
    obj = FreeBSD(sysdescr)
    if obj.parse():
        return obj
    #
    # iij seil
    #
    obj = IIJSeil(sysdescr)
    if obj.parse():
        return obj
    #
    # yamaha rtx
    #
    obj = YamahaRTX(sysdescr)
    if obj.parse():
        return obj
    #
    # Unknown
    #
    obj = Unknown(sysdescr)
    if obj.parse():
        return obj

    return None
