# -*- coding: utf-8 -*-

"""sysdescrparser."""


# Why this?
# import sys
# import os
# sys.path.append(os.path.dirname(__file__))

from sysdescrparser.aruba import Aruba
from sysdescrparser.cisco_asa import CiscoASA
from sysdescrparser.cisco_ios import CiscoIOS
from sysdescrparser.cisco_nxos import CiscoNXOS
from sysdescrparser.cisco_iosxe import CiscoIOSXE
from sysdescrparser.cisco_iosxr import CiscoIOSXR
from sysdescrparser.mikrotik_routeros import MikroTikRouterOS
from sysdescrparser.juniper_junos import JuniperJunos
from sysdescrparser.juniper_screenos import JuniperScreenOS
from sysdescrparser.brocade_ironware import BrocadeIronWare
from sysdescrparser.brocade_serveriron import BrocadeServerIron
from sysdescrparser.brocade_networkos import BrocadeNetworkOS
from sysdescrparser.foundry_ironware import FoundryIronWare
from sysdescrparser.arista_eos import AristaEOS
from sysdescrparser.hp_procurve import HPProCurve
from sysdescrparser.extreme_xos import ExtremeXOS
from sysdescrparser.paloalto_panos import PaloAltoPANOS
from sysdescrparser.a10_acos import A10ACOS
from sysdescrparser.citrix_netscaler import CitrixNetscaler
from sysdescrparser.linux import Linux
from sysdescrparser.sun_sunos import SunSUNOS
from sysdescrparser.freebsd import FreeBSD
from sysdescrparser.iij_seil import IIJSeil
from sysdescrparser.yamaha_rtx import YamahaRTX
from sysdescrparser.fortinet_fortios import FortiOs
from sysdescrparser.unknown import Unknown


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
    # aruba
    #
    obj = Aruba(sysdescr)
    if obj.parse():
        return obj
    #
    # cisco asa
    #
    obj = CiscoASA(sysdescr)
    if obj.parse():
        return obj
    #
    # cisco nxos
    #
    obj = CiscoNXOS(sysdescr)
    if obj.parse():
        return obj
    #
    # cisco iosxe
    #
    obj = CiscoIOSXE(sysdescr)
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
    # mikrotik routeros
    obj = MikroTikRouterOS(sysdescr)
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
    # fortigate
    #
    obj = FortiOs(sysdescr)
    if obj.parse():
        return obj
    #
    # Unknown
    #
    obj = Unknown(sysdescr)
    if obj.parse():
        return obj

    return None
