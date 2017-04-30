import unittest

from tests import load_fixture_nb
from dissertate.preprocessors import AddAuthors, EmptyCellElider, CellElider


class TestAddAuthors(unittest.TestCase):

    def test_add_authors(self):
        nb = load_fixture_nb("basic")
        f = AddAuthors()

        nb_, _ = f.preprocess(nb, [])
        self.assertNotIn('authors', nb_['metadata'])

        f.authors = ['Jack', 'Jill']
        nb_, _ = f.preprocess(nb, [])
        self.assertIn('authors', nb_['metadata'])
        self.assertEqual(nb_['metadata']['authors'],
                         [{'name': 'Jack'}, {'name': 'Jill'}])


class TestEmptyCellElider(unittest.TestCase):
    def test_empty_cell_elider(self):
        cells = [{'source': ' '},
                 {'source': 'A'},
                 {'source': 'B'},
                 {'nosource': '\t'}]

        nb, _ = EmptyCellElider().preprocess({'cells': cells}, None)
        source = [cell['source'] for cell in nb['cells']]
        self.assertEqual("".join(source), "AB")



class TestCellElider(unittest.TestCase):
    def test_cell_elider(self):
        cells = [{'source': 'a', 'outputs': ['A']},
                 {'source': 'b', 'outputs': ['B'],
                  'metadata': {'tags': ['private']}},
                 {'source': 'c', 'outputs': ['C'],
                  'metadata': {'tags': ['setup']}},
                 {'source': 'd', 'outputs': ['D'],
                  'metadata': {'tags': ['output-generator']}},
                 {'source': 'e', 'outputs': ['E'],
                  'metadata': {'tags': ['run-verified-code']}},
                 {'source': 'f', 'outputs': ['F']}]

        nb, _ = CellElider().preprocess({'cells': cells}, None)
        source, outputs = [], []
        for cell in nb['cells']:
            source.append(cell['source'])
            outputs.extend(cell['outputs'])
        self.assertEqual("".join(source), "aef")
        self.assertEqual("".join(outputs), "ADF")


if __name__ == '__main__':
    unittest.main()
