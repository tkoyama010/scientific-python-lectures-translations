# basedir is set by <lang>/conf.py
"""
Use "-D language=<LANG>" option to build a localized scientific-python-lectures document.

For example::

    sphinx-build -D language=ja -b html . _build/html

This conf.py does:
- Specify `locale_dirs`.
- Overrides source directory as 'scientific-python-lectures`.

"""

from pathlib import Path
import importlib.util
import importlib.machinery

basedir = Path(__file__).resolve().parent / "scientific-python-lectures"
spec = importlib.util.spec_from_file_location("conf", basedir / "conf.py")
conf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(conf)
locale_dirs = [basedir / "../locale/"]


def setup(app) -> None:  # noqa: D103,ANN001
    app.srcdir = basedir
    app.confdir = app.srcdir
