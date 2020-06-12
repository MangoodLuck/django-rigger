r"""
______  _____  _____   _____  ______ ______
| ___ \|_  _| __    \| __    \  ____\ | ___ \
| |_/ / | | | |  ___ | |  ___\ \____ | |_/ /
|    /  | | | |  __ \ |  __  \ \____\|    /
| |\ \ _| |_\ \___/ \ \___/  \ \____ | |\ \
\_| \_|____| \ ____/ \ ____/ \______ \_| \_|

"""

__title__ = 'Django Rigger'
__version__ = '1.0'
__author__ = 'Xiao Man'
__license__ = 'BSD 3-Clause'
__copyright__ = 'Copyright 2020-2025 Encode Mangood'

# Version synonym
VERSION = __version__

# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING = 'iso-8859-1'

# Default datetime input and output formats
ISO_8601 = 'iso-8601'

default_app_config = 'rigger.apps.RiggerworkConfig'


class RemovedInDRF313Warning(DeprecationWarning):
    pass


class RemovedInDRF314Warning(PendingDeprecationWarning):
    pass

