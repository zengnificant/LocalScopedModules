import os
from os.path import isdir
from os import listdir
from .settings_utils import get_projects, get_scope_prefix

sep = os.sep


def delete_slash_at_end(path):
    while True:
        lenlen = len(path)
        if path.endswith(sep):
            path = path[:lenlen - 1]
        else:
            break
    return path


def get_cur_proj(filename):
    projects = get_projects()
    ret_projects = []
    for proj in projects:
        if 'project_root' in proj:
            project_root = delete_slash_at_end(proj['project_root'])
            if project_root in filename:
                ret_projects.append(proj)
    if not len(ret_projects):
        return
    cur_proj_root = ''
    cur_proj_index = 0
    proj_index = 0
    for project in ret_projects:
        project_root = project['project_root']
        if cur_proj_root in project_root:
            cur_proj_root = project_root
            cur_proj_index = proj_index
        proj_index += 1
    cur_proj = ret_projects[cur_proj_index]
    cur_proj['project_root'] = delete_slash_at_end(cur_proj['project_root'])
    return cur_proj


def get_scopes(filename):
    proj = get_cur_proj(filename)
    if not proj:
        return
    if 'scopes' in proj:
        return proj['scopes']
    return


def is_valid_root(str, root_prefix):
    if str.startswith(root_prefix + sep) and str.count(root_prefix) == 1:
        return True
    return False


def is_valid_scope(str, scope_name):
    if str.startswith(scope_name + sep) and str.count(scope_name) == 1:
        return True
    if str == scope_name:
        return True
    return False


def sorted_dir_files(cur_path, sep):
    if not cur_path or not isdir(cur_path):
        return
    dir_files = listdir(cur_path)
    dir_files = [d for d in dir_files if not d.startswith('.')]
    dirs = sorted([d + sep for d in dir_files if not '.' in d],
                  key=lambda d: d[0])
    files = sorted([d for d in dir_files if '.' in d], key=lambda d: d[0])
    dirs.extend(files)
    dir_files = dirs
    return dir_files
