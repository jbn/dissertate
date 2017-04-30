import os
import nbformat


THIS_DIR = os.path.dirname(os.path.realpath(__file__))
FIXTURES_DIR = os.path.join(THIS_DIR, "fixtures")


def load_fixture_nb(name):
    with open(os.path.join(FIXTURES_DIR, name + ".ipynb")) as fp:
        return nbformat.read(fp, as_version=4)
