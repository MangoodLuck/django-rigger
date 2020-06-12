"""
Settings for Rigger are all namespaced in the RIGGER setting.
For example your project's `settings.py` file might look like this:
RIGGER = {
    'DEFAULT_RE_CLASSES': [
        'rigger.JSONRenderer',
        'rigger.HTMLRenderer',
    ],
    'DEFAULT_RE_CLASSES': [
        'rigger.parsers.JSONParser',
        'rigger.parsers.MultiPartParser',
    ],
}
This module provides the `api_setting` object, that is used to access
Rigger settings, checking for user settings first, then falling
back to the defaults.
"""

from django.conf import settings
from django.test.signals import setting_changed
from django.utils.module_loading import import_string

from rest_framework import ISO_8601

DEFAULTS = {
    'DEFAULT_RENDERER_CLASSES': [
        'rigger.renderers.JSONRenderer',
        'rigger.renderers.BrowsableAPIRenderer',
    ],
}


# List of settings that may be in string import notation.
IMPORT_STRINGS = [

]


# List of settings that have been removed
REMOVED_SETTINGS = [

]


def perform_import(val, setting_name):
    """
    If the given setting is a string import notation,
    then perform the necessary import or imports.
    """
    if val is None:
        return None
    elif isinstance(val, str):
        return import_from_string(val, setting_name)
    elif isinstance(val, (list, tuple)):
        return [import_from_string(item, setting_name) for item in val]
    return val


def import_from_string(val, setting_name):
    """
    Attempt to import a class from a string representation.
    """
    try:
        return import_string(val)
    except ImportError as e:
        msg = "Could not import '%s' for API setting '%s'. %s: %s." % (val, setting_name, e.__class__.__name__, e)
        raise ImportError(msg)


class APISettings:
    """
    A settings object that allows RIGGER settings to be accessed as
    properties. For example:
        from rigger.settings import api_settings
        print(api_settings.DEFAULT_RENDERER_CLASSES)
    Any setting with string import paths will be automatically resolved
    and return the class, rather than the string literal.
    Note:
    This is an internal class that is only compatible with settings namespaced
    under the RIGGER name. It is not intended to be used by 3rd-party
    apps, and test helpers like `override_settings` may not work as expected.
    """
    def __init__(self, user_settings=None, defaults=None, import_strings=None):
        if user_settings:
            self._user_settings = self.__check_user_settings(user_settings)
        self.defaults = defaults or DEFAULTS
        self.import_strings = import_strings or IMPORT_STRINGS
        self._cached_attrs = set()

    @property
    def user_settings(self):
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, 'RIGGER', {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid API setting: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Coerce import strings into classes
        if attr in self.import_strings:
            val = perform_import(val, attr)

        # Cache the result
        self._cached_attrs.add(attr)
        setattr(self, attr, val)
        return val

    def __check_user_settings(self, user_settings):
        SETTINGS_DOC = "https://www.django-rigger.org/api-guide/settings/"
        for setting in REMOVED_SETTINGS:
            if setting in user_settings:
                raise RuntimeError("The '%s' setting has been removed. Please refer to '%s' for available settings." % (setting, SETTINGS_DOC))
        return user_settings

    def reload(self):
        for attr in self._cached_attrs:
            delattr(self, attr)
        self._cached_attrs.clear()
        if hasattr(self, '_user_settings'):
            delattr(self, '_user_settings')


api_settings = APISettings(None, DEFAULTS, IMPORT_STRINGS)


def reload_api_settings(*args, **kwargs):
    setting = kwargs['setting']
    if setting == 'RIGGER':
        api_settings.reload()


setting_changed.connect(reload_api_settings)