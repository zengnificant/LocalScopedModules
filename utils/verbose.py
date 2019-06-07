
from sublime import Region
from .editor_utils import Scope_cache


def get_current_line(view, a):
    current_line = view.full_line(a)
    return current_line


def get_next_line(view, a):
    next_line_start = get_current_line(view, a).b
    next_line = view.full_line(next_line_start)
    return next_line


def verbose_new_line(view, edit, scope=None):
    scope = Scope_cache.get_scope()
    if not scope:
        return
    sel = view.sel()[0].a
    next_line = get_next_line(view, sel)
    next_line_str = view.substr(next_line)
    content = '//' + scope['name'] + ' : ' + scope['dir']
    ret_line = content + '\n'
    if next_line_str != ret_line:
        view.insert(edit, next_line.a, ret_line)
    next2_line = get_next_line(view, next_line.a)
    next2_line_str = view.substr(next2_line)
    if not next2_line_str == '\n':
        view.insert(edit, next2_line.a, '\n')
    new_next_line = get_next_line(view, sel)
    view.sel().clear()
    new_region = Region(new_next_line.a, new_next_line.b - 1)
    view.sel().add(new_region)

#
