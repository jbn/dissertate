from nbconvert.preprocessors import Preprocessor
from traitlets import Unicode, List


class AddAuthors(Preprocessor):
    """
    Add author names to each notebook.
    """
    authors = List(Unicode)

    def preprocess(self, nb, resources):
        if self.authors:
            authors = [{'name': author} for author in self.authors]
            nb['metadata']['authors'] = authors
        return nb, resources


class ElideCell(Exception):
    pass


def elide_fully(cell):
    raise ElideCell()


def clear_source(cell):
    cell['source'] = ''


def clear_outputs(cell):
    cell['outputs'] = []



class EmptyCellElider(Preprocessor):
    def preprocess(self, nb, resources):
        new_cells = []

        for cell in nb['cells']:
            if cell.get('source', '').strip():
                new_cells.append(cell)

        nb['cells'] = new_cells

        return nb, resources



class CellElider(Preprocessor):
    elide_fully_tags = List(Unicode(), default_value=['private',
                                                      'setup',
                                                      'todo'])
    clear_source_tags = List(Unicode(), default_value=['output-generator'])
    clear_output_tags = List(Unicode(), default_value=['run-verified-code'])

    def preprocess(self, nb, resources):
        rules = {}

        for k in self.elide_fully_tags:
            rules[k] = elide_fully

        for k in self.clear_source_tags:
            rules[k] = clear_source

        for k in self.clear_output_tags:
            rules[k] = clear_outputs

        new_cells = []

        for cell in nb['cells']:
            try:
                for tag in cell.get('metadata', {}).get('tags', []):
                    f = rules.get(tag)
                    if f:
                        f(cell)
                new_cells.append(cell)
            except ElideCell:
                pass

        nb['cells'] = new_cells

        return nb, resources
