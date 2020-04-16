from sublime import Region
from sublime_plugin import EventListener, TextCommand
import os
from os.path import isdir
from os import listdir
from .utils.editor_utils import get_source_at_sel, get_cur_path
from .utils.str_utils import get_prefix,  get_quote
from .utils.paths import get_cur_proj, get_scopes, sorted_dir_files
from .utils.settings_utils import get_verbose, get_scope_prefix
from .utils.verbose import verbose_new_line
sep = os.sep


class lsmVerboseCommand(TextCommand):

    def run(self, edit):
        view = self.view
        verbose_new_line(view, edit)


class LSMComplete(EventListener):

    def on_pre_save(self, view):
        verbose = get_verbose()
        if not verbose:
            return
        cur_path = get_cur_path(view)
        if not cur_path:
            return
        view.run_command('lsm_verbose')

    def on_selection_modified_async(self, view):

        if not view.window():
            return
        sel = view.sel()[0]
        if not sel.empty():
            return

        source = get_source_at_sel(view)

        if not source:
            return

        scope_prefix = get_scope_prefix()
        if source == scope_prefix:
            view.run_command('auto_complete',
                             {'disable_auto_insert': True,
                              'next_completion_if_showing': False})
            return

        cur_path = get_cur_path(view)
        if not cur_path:
            return

        if not isdir(cur_path):
            return
        if view.substr(sel.a - 1) == sep:
            view.run_command('auto_complete',
                             {'disable_auto_insert': True,
                              'next_completion_if_showing': False})

    def on_modified_async(self, view):
        view.run_command('hide_auto_complete',
                         {'disable_auto_insert': True,
                          'next_completion_if_showing': False})

    def on_query_completions(self, view, prefix, locations):
        completions = []
        scope_prefix = get_scope_prefix()
        filename = view.file_name()
        scopes = get_scopes(filename)
        if not scopes:
            return
        source = get_source_at_sel(view)
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
