from django.conf import settings
from django.test.signals import setting_changed

from djgraphql.defaults import Defaults


class ImportSettings:
    @staticmethod
    def defaults():
        params = {key:value for key, value in Defaults.__dict__.items() if not key.startswith('__') and not callable(key)}
        new_defaults = {}
        for key, value in params.items():
            try:
                new_defaults[key] = getattr(settings, key, value)
            except Exception as e:  # noqa
                new_defaults[key] = value
        return new_defaults


DEFAULTS = ImportSettings.defaults()


class APISettings:
    """
    A settings object that allows REST Framework settings to be accessed as
    properties. For example:
        from common.settings import api_settings
        print(api_settings.ACCEPTED_DOCUMENT_FORMATS)
    Any setting with string import paths will be automatically resolved
    and return the class, rather than the string literal.
    Note:
    This is an internal class that is only compatible with settings namespaced
    under the COMMON name. It is not intended to be used by 3rd-party
    apps, and test helpers like `override_settings` may not work as expected.
    """

    def __init__(self, defaults=None):
        self.defaults = defaults or DEFAULTS
        self._cached_attrs = set()

    @property
    def user_settings(self):
        if not hasattr(self, '_user_settings'):
            setattr(self, '_user_settings', self.defaults)
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid API setting: '%s'" % attr)
        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            raise ValueError(f'Invalid setting variable: {attr}')
        # Cache the result
        self._cached_attrs.add(attr)
        setattr(self, attr, val)
        return val

    def reload(self):
        for attr in self._cached_attrs:
            delattr(self, attr)
        self._cached_attrs.clear()
        if hasattr(self, '_user_settings'):
            delattr(self, '_user_settings')


api_settings = APISettings(DEFAULTS)


def reload_api_settings(*args, **kwargs):
    setting = kwargs['setting']
    if setting.lower() == 'common':
        api_settings.reload()


setting_changed.connect(reload_api_settings)
