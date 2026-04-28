import json
from pathlib import Path

from bs4 import BeautifulSoup


# File types
class Format(object):
    """Template for a specific file type; renders and
    writes out to file.

    For text formats, simply override the templates
    below. For other formats, override `render`
    and `write`.

    `render` should return an object whose string
    representation is a fully valid document of
    that format.
    """

    template = "{title}\n\n{sections}\n\n{docs_link}"
    append_delimiter = "\n\n"

    section_template = "{title}\n{lines}"
    section_delimiter = "\n\n"

    line_template = "* {line_id} {line_summary}: {line}"
    line_delimiter = "\n"
    docs_link = "Data Science Ethics Checklist generated with deon (http://deon.drivendata.org)."
    badge = None

    def __init__(self, checklist):
        self.checklist = checklist

    def render(self):
        """Uses the checklist and templates to render
        all of the components for this format.
        """
        pass

    def write(self, filepath, overwrite=False):
        """Renders template and writes to `filepath`."""
        pass


class Markdown(Format):
    """Markdown template items"""

    template = "# {title}\n{badge}\n{sections}\n\n{docs_link}"
    section_template = """## {title}
{lines}"""

    line_template = " - [ ] **{line_id} {line_summary}**: {line}"
    docs_link = (
        "*Data Science Ethics Checklist generated with [deon](http://deon.drivendata.org).*"
    )
    badge = """
[![Deon badge](https://img.shields.io/badge/ethics%20checklist-deon-brightgreen.svg?style=popout-square)](http://deon.drivendata.org/)
"""


class Rst(Format):
    """reStructuredText template items"""

    template = "{title}\n============\n\n{badge}\n\n{sections}\n\n{docs_link}"
    section_template = """{title}\n---------\n\n{lines}"""
    line_template = "* [ ] **{line_id} {line_summary}**: {line}"
    docs_link = (
        "*Data Science Ethics Checklist generated with* `deon <http://deon.drivendata.org>`_."
    )
    badge = """.. image:: https://img.shields.io/badge/ethics%20checklist-deon-brightgreen.svg?style=popout-square
   :target: http://deon.drivendata.org"""


class JsonDict(dict):
    """Suclass of dict with valid json string representation."""

    def __str__(self):
        pass

    def __repr__(self):
        pass


class JupyterNotebook(Markdown):
    """Jupyter notebook template items"""

    append_delimiter = {"cell_type": "markdown", "metadata": {}, "source": ["-----\n"]}

    def render(self):
        """Creates json for a valid blank Jupyter notebook with a cell
        containing the rendered Markdown of the checklist.
        """
        pass

    def write(self, filepath, overwrite=False):
        """If notebook does not exist (or `overwrite=True`), write new
        notebook with checklist. Otherwise append a cell with a
        horizontal rule and another cell with the checklist.
        """
        pass


class JupyterNotebookMulticell(JupyterNotebook):
    """Jupyter notebook multiple cell format"""

    def render(self):
        pass


class Html(Format):
    """HTML template items"""

    template = """<h1>{title}</h1>
<br/> <br/>
{badge}
<br/> <br/>
{sections}
<br/> <br/>
<em>Data Science Ethics Checklist generated with <a href="http://deon.drivendata.org">deon.</a></em>"""
    section_template = """<h2>{title}</h2>
<hr/>
<ul>
{lines}
</ul>"""

    section_delimiter = """
<br/>
"""

    line_template = (
        "<li><input type='checkbox'><strong>{line_id} {line_summary}:</strong> {line}</input></li>"
    )
    line_delimiter = "\n"
    badge = """
<a href="http://deon.drivendata.org/">
    <img
        src="https://img.shields.io/badge/ethics%20checklist-deon-brightgreen.svg?style=popout-square"
        alt="Deon badge"
    />
</a>
    """
    doc_template = """<html>
<body>
{text}
</body>
</html>
"""

    def render(self):
        """Create a new blank HTML document with checklist as the body."""
        pass

    def write(self, filepath, overwrite=False):
        """If html document does not exist (or `overwrite=True`), write new
        html file with checklist.
        """
        pass


FORMATS = {
    "ascii": Format,
    "html": Html,
    "jupyter": JupyterNotebook,
    "jupyter-multicell": JupyterNotebookMulticell,
    "markdown": Markdown,
    "rmarkdown": Markdown,
    "rst": Rst,
}

# keep all extensions lowercase
EXTENSIONS = {
    ".txt": "ascii",
    ".html": "html",
    ".ipynb": "jupyter",
    ".md": "markdown",
    ".rmd": "rmarkdown",
    ".rst": "rst",
}
