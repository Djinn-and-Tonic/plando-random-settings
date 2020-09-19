__version__ = "5.2.54 R-2 v1"
version_hash_1 = "Mask of Truth"
version_hash_2 = "Mask of Truth"


class VersionError(Exception):
    def __init__(self, cause):
        message = f"Your {cause} is out of date. Please update it before continuing."
        with open('blind_random_settings.json', 'w') as fp:
            fp.write(message)
        super().__init__(message)


def check_rando_version():
    from version import __version__ as roman_version
    rmajor, rminor, rfix = roman_version.split()[0].split('.')
    rver = roman_version.split()[1]

    major, minor, fix = __version__.split()[0].split('.')
    ver, sver = __version__.split()[1:]

    if int(rmajor) != int(major) or int(rminor) != int(minor) or int(rfix) < int(fix):
        raise VersionError("dev-R or rando rando script")
    if int(rver[-1]) < int(ver[-1]):
        raise VersionError("dev-R")