
from sublime import Region


def get_current_line(view, a):
    current_line = view.full_line(a)
    return current_line


def get_next_line(view, a):
    next_line_start = get_current_line(view, a).b
    next_line = view.full_line(next_line_start)
    return next_line


def new_line_not_empty(view, edit, enable_max_skip=True):
    sel = view.sel()[0].a
    next_line = get_next_line(view, sel)
    count = 0
    max_skip = 5
    while view.substr(next_line.a) == '\n':
        sel = next_line.b
        next_line = get_next_line(view, sel)
        if enable_max_skip:
            if count >= 5:
                break
            count += 1
    return next_line
