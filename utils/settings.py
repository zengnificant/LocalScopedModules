from sublime import load_settings
SETTINGS_FILENAME = 'LocalScopedModules.sublime-settings'


def get_pref(key):
    """get value under the given name key from the settings file"""
    return load_settings(SETTINGS_FILENAME).get(key)
