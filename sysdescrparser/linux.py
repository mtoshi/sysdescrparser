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
        "ubuntu": {
            "ubuntu": "",
            "lucid": "10.04",
            "precise": "12.04",
            "trusty": "14.04",
            "xenial": "16.04",
            "bionic": "18.04"
        },
        "centos": {
            "centos": "",
            "centos6": "6.0",
            "el6": "6.0",
            "centos7": "7.0",
            "el7": "7.0"
        }
    }

    def __init__(self, raw):
        """Constructor."""
        super(Linux, self).__init__(raw)
        self.vendor = self.UNKNOWN
        self.model = self.UNKNOWN
        self.os = 'LINUX'
        self.version = self.UNKNOWN

    def parse(self):
        """Parsing for sysDescr value."""
        regex = (r'^Linux\s+')
        pat = re.compile(regex)
        res = pat.search(self.raw)
        if res:
            regex = (r'\s+')
            pat = re.compile(regex)
            res = pat.split(self.raw)
            if len(res) > 2:
                kernel_version = res[2]

            ubuntu_version_names_regex = os_version_names_regex(self.__class__.versions["ubuntu"])
            ubuntu_match = re.search(
                            ubuntu_version_names_regex,
                            self.raw,
                            flags=re.IGNORECASE
                           )

            centos_version_names_regex = os_version_names_regex(self.__class__.versions["centos"])
            centos_match = re.search(
                            centos_version_names_regex,
                            self.raw,
                            flags=re.IGNORECASE
                           )

            version_name = ""
            if ubuntu_match:
                self.vendor = "CANONICAL"
                self.os = "UBUNTU"
                version_name = ubuntu_match.group()

            if centos_match:
                self.vendor = "CENTOS"
                self.os = "CENTOS"
                version_name = centos_match.group()

            if version_name:
                # make it lower cause our versions dict keys are lower
                os_lookup_name = self.os.lower()
                os_versions = self.__class__.versions[os_lookup_name]
                version_number = extract_version_number(
                    os_versions,
                    version_name,
                )
                if version_number:
                    self.version = version_number
                    self.model = kernel_version

                else:
                    self.version= kernel_version


            else:
                self.version = kernel_version

            return self

        return False
