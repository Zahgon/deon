import os
from pathlib import Path

from .formats import EXTENSIONS, FORMATS
from .parser import Checklist

DEFAULT_CHECKLIST = Path(__file__).parent / "assets" / "checklist.yml"

CHECKLIST_FILE = Path(os.environ.get("ETHICS_CHECKLIST", DEFAULT_CHECKLIST))


class ExtensionException(Exception):
    pass


class FormatException(Exception):
    pass


class MulticellException(Exception):
    pass


def create(checklist, output_format, output, overwrite, multicell):
    pass
