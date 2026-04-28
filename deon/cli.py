import click

from .deon import ExtensionException, FormatException, MulticellException, create
from .formats import EXTENSIONS


@click.command("deon")
@click.option(
    "--checklist",
    "-l",
    default=None,
    type=click.Path(exists=True),
    help="Override default checklist file with a path to a custom checklist.yml file.",
)
@click.option(
    "--format",
    "-f",
    "output_format",
    default=None,
    type=str,
    help='Output format. Default is "markdown". '
    + "Can be one of [{}]. ".format(", ".join(["ascii", "html", "jupyter", "jupyter-multicell", "markdown", "rmarkdown", "rst"]))
    + "Ignored and file extension used if --output is passed.",
)
@click.option(
    "--output",
    "-o",
    default=None,
    type=click.Path(),
    help="Output file path. Extension can be one of [{}]. ".format(", ".join([".txt", ".html", ".ipynb", ".md", ".rmd", ".rst"]))
    + "The checklist is appended if the file exists.",
)
@click.option(
    "--overwrite",
    "-w",
    is_flag=True,
    default=False,
    help="Overwrite output file if it exists. "
    + "Default is False, which will append to existing file.",
)
@click.option(
    "--multicell",
    "-m",
    is_flag=True,
    default=False,
    help="For use with Jupyter format only. "
    + "Write checklist with multiple cells, one item per cell. "
    + "Default is False, which will write the checklist in a single cell.",
)
def main(checklist, output_format, output, overwrite, multicell):
    """Easily create an ethics checklist for your data science project.

    The checklist will be printed to standard output by default. Use the --output option to write
    to a file instead.
    """
    pass


if __name__ == "__main__":
    main()
