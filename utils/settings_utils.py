from .settings import get_pref


def get_root_prefix():
    return get_pref('lsm_root_prefix')


def get_scope_prefix():
    return get_pref('lsm_scope_prefix')


def get_verbose():
    return get_pref('lsm_verbose')


def get_projects():
    return get_pref('lsm_projects')
