
from sublime import Region


def get_current_line(view, a):
    current_line = view.full_line(a)
    return current_line


def get_next_line(view, a):
    next_line_start = get_current_line(view, a).b
    next_line = view.full_line(next_line_start)
    return next_line


scope = {"dir": "~/babel-plugin", "name": "@plugin"}


def verbose_new_line(view, edit, scope=scope):
    sel = view.sel()[0].a
    next_line = get_next_line(view, sel)
    next_line_str = view.substr(next_line)
    content = '//' + scope['name'] + ' : ' + scope['dir']
    ret_line = content + '\n'
    if not next_line_str.startswith(content):
        view.insert(edit, next_line.a, ret_line)
    next2_line = get_next_line(view, next_line.a)
    next2_line_str = view.substr(next2_line)
    if not next2_line_str == '\n':
        view.insert(edit, next2_line.a, '\n')
    view.sel().clear()
    view.sel().add(next_line)

#
