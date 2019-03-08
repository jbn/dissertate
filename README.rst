.. image:: https://travis-ci.org/jbn/dissertate.svg?branch=master
    :target: https://travis-ci.org/jbn/dissertate
.. image:: https://ci.appveyor.com/api/projects/status/69kj3prrrieyp8q2/branch/master?svg=true
    :target: https://ci.appveyor.com/project/jbn/dissertate/branch/master 
.. image:: https://coveralls.io/repos/github/jbn/dissertate/badge.svg?branch=master
    :target: https://coveralls.io/github/jbn/dissertate?branch=master 
.. image:: https://img.shields.io/pypi/v/dissertate.svg
    :target: https://pypi.python.org/pypi/dissertate
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://raw.githubusercontent.com/jbn/dissertate/master/LICENSE
.. image:: https://img.shields.io/pypi/pyversions/dissertate.svg
    :target: https://pypi.python.org/pypi/dissertate

Installation
------------

.. code:: sh

   pip install dissertate


Basic Usage
-----------

In ``nb_config.py``,

.. code:: python

   import dissertate

   c = get_config()

   c.Exporter.preprocessors = ['dissertate.preprocessors.EmptyCellElider',
                               'dissertate.preprocessors.CellElider']

   c.Exporter.template_file = dissertate.markdown_template_path()

then,

.. code:: sh

   jupyter nbconvert --config nb_config.py --to markdown your_nb.ipynb

If you don't want a cell in the output, edit the cell metadata to include,

.. code:: json

   {"tags": ["private"]}

If you want the output of the cell but not the code, 

.. code:: json

   {"tags": ["output-generator"]}

