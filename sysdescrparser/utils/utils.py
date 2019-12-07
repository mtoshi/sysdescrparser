def os_version_names_regex(os_dict):
    os_version_names = os_dict.keys()
    return "|".join(os_version_names)


def extract_version_number(os_dict, version_name):
    version_name = version_name.lower()
    version_number = os_dict[version_name]
    version_number = str(version_number)
    return version_number
