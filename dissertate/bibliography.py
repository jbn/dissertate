import os
import bibtexparser
from dissertate.util import walk_paths


def walk_bibs(base_dir):
    for parts in walk_paths("."):
        if parts[0].lower().endswith('.bib'):
            yield parts


class Bibliography:
    def __init__(self, base_dir):
        self._root_dir = os.path.abspath(base_dir)
        self._bibs = {}

        for file_name, path, base_dir in walk_bibs("."):
            with open(path) as bibtex_file:
                bib = bibtexparser.load(bibtex_file)
            self._bibs[path] = bib

    @property
    def root_dir(self):
        return self._root_dir

    def iterate_entries(self):
        for bib_db in self._bibs.values():
            for entry in bib_db.entries:
                yield entry

    @property
    def all_entries(self):
        return list(self.iterate_entries())

    def simple_search(self, k, q, with_bibpath=True):
        q = q.lower()
        # See conventions for capitalization:
        # https://bibtexparser.readthedocs.io/en/v0.6.2/tutorial.html
        for path, bib_db in self._bibs.items():
            for entry in bib_db.entries:
                v = entry.get(k, '')
                if v and q in v.lower():
                    d = {k: v for k, v in entry.items()}
                    if with_bibpath:
                        full_path = os.path.join(self.root_dir, path)
                        d['bib_path'] = os.path.normpath(full_path)
                    yield d


if __name__ == '__main__':
    bib = Bibliography(os.getcwd())
    print("Scanning from:", bib.root_dir)
    for entry in bib.all_entries:
        print(entry)
