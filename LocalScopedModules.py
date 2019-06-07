from sublime import Region

from sublime_plugin import EventListener, TextCommand
import os
from os.path import isdir
from os import listdir
from .utils.editor_utils import get_source_at_sel, get_cur_path
from .utils.str_utils import get_prefix,  get_quote
from .utils.paths import get_cur_proj, get_scopes, sorted_dir_files

from .utils.settings import get_pref
from .utils.verbose import new_line_not_empty
sep = os.sep


class removeNextLineCommand(TextCommand):

    def run(self, edit):
        view = self.view
        next_line = new_line_not_empty(view, edit)
        strings = view.substr(next_line)
        print([strings])


class LSMComplete(EventListener):

    def on_pre_save(self, view):
        source = get_source_at_sel(view)
        if not source:
            return
        view.run_command('remove_next_line')

    def on_selection_modified_async(self, view):

        if not view.window():
            return
        sel = view.sel()[0]
        if not sel.empty():
            return
        cur_path = get_cur_path(view)
        if not cur_path:
            return

        if not isdir(cur_path):
            return
        if view.substr(sel.a - 1) == sep:
            view.run_command('auto_complete', {
                'disable_auto_insert': True, 'next_completion_if_showing': False})

    def on_query_completions(self, view, prefix, locations):
        source = get_source_at_sel(view)
        if not source:
            return
        completions = []
        prefix = get_prefix(source)
        scope_prefix = get_pref('lsm_scope_prefix')
        filename = view.file_name()
        scopes = get_scopes(filename)
        if not scopes:
            return
        if source == scope_prefix:
            if not scopes or not len(scopes):
                return
            for scope in scopes:
                if type(scope) == dict and 'name' in scope and 'dir' in scope:
                    scope_name = scope['name']
                    scope_name += sep
                    completions.append([scope_name, scope_name[1:]])

            return completions
        cur_path = get_cur_path(view)
        if not cur_path:
            return
        if not isdir(cur_path):
            return
        dir_files = sorted_dir_files(cur_path, sep)
        if not dir_files or not len(dir_files):
            return
        for d in dir_files:
            completions.append([d, d])
        return completions
