import os
from pathlib import Path


def print_file_or_dir(path, indent=0):
    name = Path(path).name
    if os.path.isdir(path):
        print(f"{' ' * indent}{name}/")
    else:
        print(f"{' ' * indent}{name}")


INDENT_PER_LEVEL = 4


def dir_tree(rel_path, indent=0):
    path = Path.cwd() / rel_path
    print_file_or_dir(path, indent=indent)
    for entry in sorted(list(os.scandir(path.as_posix())), key=lambda e: e.name.lower()):
        if entry.is_file():
            print_file_or_dir(entry.name, indent=indent + INDENT_PER_LEVEL)
        elif entry.is_dir():
            dir_tree(entry.path, indent=indent + INDENT_PER_LEVEL)
