# -*- coding: utf-8 -*-

"""sysdescrparser.linux."""

import re
from sysdescr import SysDescr
from utils.utils import os_version_names_regex, extract_version_number


# pylint: disable=no-name-in-module
# pylint: disable=no-member
class Linux(SysDescr):

    """Class Linux.

    This class is only for vendor definition.

    """

    versions = {
        "ubuntu_linux": {
            "lucid": "10.04",
            "precise": "12.04",
            "trusty": "14.04",
            "xenial": "16.04",
            "bionic": "18.04",
        },
        "centos": {
            "centos6": "6.0",
            "el6": "6.0",
            "centos7": "7.0",
            "el7": "7.0",
            "centos": "",
        }
    }

    def __init__(self, raw):
        """Constructor."""
        super(Linux, self).__init__(raw)
        self.vendor = 'LINUX'
        self.model = self.UNKNOWN
        self.os = 'LINUX_KERNEL'
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        version_name = ""
        kernel_version = ""

        regex = (r'^Linux\s+')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            regex = (r'\s+')
            pat = re.compile(regex)
            res = pat.split(self.raw)
            if len(res) > 2:
                kernel_version = res[2]

            ubuntu_version_names_regex = os_version_names_regex(self.__class__.versions["ubuntu_linux"])
            ubuntu_lts_match = re.search(
                            ubuntu_version_names_regex,
                            self.raw,
                            flags=re.IGNORECASE
                           )
            ubuntu_main_version_name_match = re.search(
                                                "ubuntu",
                                                self.raw,
                                                flags=re.IGNORECASE
                                            )

            centos_version_names_regex = os_version_names_regex(self.__class__.versions["centos"])
            centos_match = re.search(
                            centos_version_names_regex,
                            self.raw,
                            flags=re.IGNORECASE
                           )

            if ubuntu_lts_match or ubuntu_main_version_name_match:
                self.vendor = "CANONICAL"
                self.os = "UBUNTU_LINUX"

                if not ubuntu_lts_match:
                    version_name = self.UNKNOWN

                else:
                    version_name = ubuntu_lts_match.group()

            if centos_match:
                self.vendor = "CENTOS"
                self.os = "CENTOS"
                version_name = centos_match.group()

            if version_name and version_name != 'UNKNOWN':
                # make it lower cause our versions dict keys are lower
                os_lookup_name = self.os.lower()
                os_versions = self.__class__.versions[os_lookup_name]
                version_number = extract_version_number(
                    os_versions,
                    version_name,
                )
                if version_number:
                    self.version = version_number

                else:
                    self.version = self.UNKNOWN

                self.model = kernel_version if kernel_version else self.UNKNOWN

            elif version_name == 'UNKNOWN':
                self.version = version_name
                self.model = kernel_version if kernel_version else self.UNKNOWN

            else:
                self.version = kernel_version

            return self

        return False
