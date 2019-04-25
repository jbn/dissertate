__title__ = "dissertate"
__author__ = "John Bjorn Nelson (generativist)"
__email__ = "jbn@abreka.com"
__description__ = "A package and CLI for writing dissertations."
__uri__ = "https://github.com/jbn/dissertate"
__doc__ = __description__ + " <" + __uri__ + ">"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2017 John Bjorn Nelson"
__version__ = "0.0.7"


def markdown_template_path():
    import os
    self_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.abspath(os.path.join(self_dir, "dissertate.tpl"))
