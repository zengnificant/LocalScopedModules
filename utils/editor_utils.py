from sublime import Region
from .str_utils import get_quote, get_prefix
from .settings_utils import get_root_prefix, get_scope_prefix
from .paths import get_cur_proj,  get_scopes, is_valid_root, is_valid_scope
import re


def get_module_specifier(strs):
    ret = re.findall(r'(import|export|require)', strs)
    if not len(ret):
        return
    return ret[-1]


def get_source_at_sel(view):

    sel = view.sel()[0].a
    name = view.scope_name(sel)
    at_string_of_js = '.js' in name and 'string.quoted' in name
    if not at_string_of_js:
        return
    current_line = view.line(sel)
    start_to_sel = Region(current_line.a, sel)
    almost_source = view.substr(start_to_sel)
    quote = get_quote(almost_source)
    source_before = almost_source[:almost_source.rfind(quote)]
    specifier = get_module_specifier(source_before)
    if not specifier:
        return
    source = almost_source[almost_source.rfind(quote) + 1:]
    prefix = get_prefix(source)
    if not prefix:
        return
    return source


class Scope_cache():
    scope = None

    @staticmethod
    def get_scope():
        return Scope_cache.scope

    @staticmethod
    def set_scope(scope):
        Scope_cache.scope = scope


def get_cur_path(view, add_path=''):
    source = get_source_at_sel(view)
    if not source:
        return
    source += add_path
    filename = view.file_name()
    cur_proj = get_cur_proj(filename)
    if not cur_proj:
        return
    project_root = cur_proj['project_root']
    prefix = get_prefix(source)
    root_prefix = get_root_prefix()
    if is_valid_root(source, root_prefix):
        return source.replace(root_prefix, project_root)
    scope_prefix = prefix
    scopes = get_scopes(filename)
    if scopes and len(scopes):
        for scope in scopes:
            if type(scope) != dict and (not 'name' in scope or not 'dir' in scope):
                Scope_cache.set_scope(None)
                return
            Scope_cache.set_scope(None)
            scope_name = scope['name']
            scope_dir = scope['dir'].replace(root_prefix, project_root)
            if is_valid_scope(source, scope_name):
                source = source.replace(scope_name, scope_dir)
                Scope_cache.set_scope(scope)
                return source
    return
