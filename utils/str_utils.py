from .settings_utils import get_root_prefix, get_scope_prefix


def get_quote(str):
    single = '\''
    double = '"'

    if single not in str and double in str:
        return double
    if single in str and double not in str:
        return single

    if single in str and double in str:
        index = min([str.find(single), str.find(double)])
        return str[index]
    return


def get_prefix(str):
    root_prefix = get_root_prefix()
    scope_prefix = get_scope_prefix()
    if str.startswith(root_prefix):
        return root_prefix

    if str.startswith(scope_prefix):
        return scope_prefix
    return
