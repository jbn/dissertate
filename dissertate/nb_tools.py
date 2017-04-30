from functools import partial
from nbformat import read as read_nb
from nbformat import write as write_nb

from dissertate.util import walk_paths


def transform(nb_path, *fs):
    with open(nb_path, "r") as fp:
        nb = read_nb(fp, as_version=4)

    for f in fs:
        f(nb)

    with open(nb_path, "w") as fp:
        write_nb(nb, nb_path)


def add_authors(nb, authors):
    nb['metadata']['authors'] = [{'name': author} for author in authors]


def update_private_meta(nb, namespace, meta_dict):
    nb['metadata'].update(meta_dict)


if __name__ == '__main__':
    working_title = "A Hacker's Guide to Heaven and Hell"

    print("Applying transformations...")
    for _, path, _ in walk_paths("."):
        if not path.lower().endswith(".ipynb"):
            continue
        print("Editing {}".format(path))
        transform(path,
                  partial(update_private_meta,
                          namespace='dissertate',
                          meta_dict={'title': working_title}),
                  partial(add_authors,
                          authors=['John Bjorn Nelson']))
