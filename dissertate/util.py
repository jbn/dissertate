import os


def walk_paths(base_dir, recursive=True, ignore_hidden=True,
               ignore_private=True):
    for file_name in os.listdir(base_dir):
        if ignore_hidden and file_name.startswith('.'):
            continue

        if ignore_private and file_name.startswith('_'):
            continue

        path = os.path.join(base_dir, file_name)

        if os.path.isdir(path):
            if recursive:
                for nb_path in walk_paths(path):
                    yield nb_path
        else:
            yield file_name, path, base_dir
